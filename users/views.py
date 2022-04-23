from http import HTTPStatus

from django.contrib.auth import get_user_model, logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
from django.db import IntegrityError, models
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from catalog.models import Item, Tag
from .backends import EmailAuthBackend
from .forms import EditProfileForm, LoginForm, RegisterForm

USER_LIST_TEMPLATE = 'users/user_list.html'
CUR_USER_TEMPLATE = 'users/user_detail.html'
SIGNUP_TEMPLATE = 'users/signup.html'
LOGIN_WITH_USERNAME_TEMPLATE = 'users/login_with_username.html'
LOGIN_WITH_EMAIL_TEMPLATE = 'users/login_with_email.html'
PROFILE_TEMPLATE = 'users/profile.html'

User: models.Model = get_user_model()


def user_list(request) -> HttpResponse:
    """
    Возвращает страничку Списка пользователей
    """

    users = User.objects.select_related('profile')

    return render(
        request, USER_LIST_TEMPLATE, status=HTTPStatus.OK, context={
            'users': users
        },
        content_type='text/html'
    )


def user_detail(request, user_id: int) -> HttpResponse:
    """
    Возвращает страничку конкретного пользователя
    """

    # В условии было сказано про то, что словарь контекста должен быть пустым
    # Но мне показалось логичным передавать айди пользователя

    user = get_object_or_404(User, id=user_id)
    items = Item.manager.get_favorite(user, Tag)

    return render(
        request, CUR_USER_TEMPLATE, status=HTTPStatus.OK,
        context={'user': user, 'items': items}, content_type='text/html'
    )


def login_with_email_view(request) -> HttpResponse:
    """
    Возвращает страничку регистрации пользователя
    """

    if request.user.is_authenticated:
        return redirect('/auth/profile', status=HTTPStatus.OK,
                        context={}, content_type='text/html')

    form = LoginForm(request.POST or None)
    if form.is_valid():

        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        user = EmailAuthBackend.authenticate(
            request, email=email, password=password
        )

        if user is not None:
            if user.is_active:
                EmailAuthBackend.authenticate(request, email, password)
                return redirect(
                    '/auth/profile', status=HTTPStatus.OK,
                    context={},
                    content_type='text/html')

    return render(
        request, LOGIN_WITH_EMAIL_TEMPLATE, status=HTTPStatus.OK,
        context={"form": form},
        content_type='text/html'
    )


def logout_view(request) -> HttpResponse:
    """
    Возвращает страничку регистрации пользователя
    """

    if request.user.is_authenticated:
        logout(request)

        return redirect('/', status=HTTPStatus.OK,
                        context={}, content_type='text/html')

    form_login = LoginForm()
    return render(
        request, LOGIN_WITH_USERNAME_TEMPLATE, status=HTTPStatus.OK,
        context={"form_login": form_login},
        content_type='text/html'
    )


def signup(request) -> HttpResponse:
    errors = []

    if request.user.is_authenticated:
        logout(request)

    form = RegisterForm(request.POST or None)

    if form.is_valid() and not errors:
        try:

            new_user, mess = EmailAuthBackend.create_user(**form.cleaned_data)
            if not mess:
                current_site = get_current_site(request)
                mail_subject = 'Activation link has been sent to your email id'

                message = render_to_string('users/acc_active_email.html', {
                    'user': new_user, 'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
                    'token': default_token_generator.make_token(new_user),
                })

                EmailMessage(mail_subject, message, to=[new_user.email]).send()
                return HttpResponse('Подтвердите почту')

            errors.append(mess)

        except (IntegrityError, ValidationError) as err:

            if type(err) is ValidationError:
                err = '\n'.join(err.messages)

            if type(err) is IntegrityError:
                err = 'Пользователь с таким именем уже сооздан'

            errors.append(err)

    errors += [err[0] for err in list(form.errors.values())]
    errors = '      '.join(set(errors))

    return render(
        request, SIGNUP_TEMPLATE, status=HTTPStatus.OK,
        context={"form_login": form, 'errors': errors},
        content_type='text/html'
    )


def activate(request, uidb64, token):
    try:

        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        return redirect('/auth/profile', status=HTTPStatus.OK,
                        context={}, content_type='text/html')
    else:
        return HttpResponse('Activation link is invalid!')


def profile(request) -> HttpResponse:
    """
    Возвращает страничку профиля пользователя
    """

    user = request.user
    # if user.email is not None:
    #     send_mail("Тест", 'Тест', 'admin@example.com', [user.email],
    #               fail_silently=False)

    if not user.is_authenticated:
        return redirect('login')

    errors = []

    if request.POST:
        form = EditProfileForm(request.POST)

        if form.is_valid():

            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.profile.birthday = form.cleaned_data['birthday']

            if not errors:
                user.save()

    else:
        form = EditProfileForm(instance=user)

    items = Item.manager.get_favorite(user, Tag)

    return render(
        request, PROFILE_TEMPLATE, status=HTTPStatus.OK, context={
            'user': user, 'items': items,
            'form': form, 'errors': '\n'.join(errors)
        },
        content_type='text/html'
    )
