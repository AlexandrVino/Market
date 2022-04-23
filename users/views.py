from http import HTTPStatus

from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.db import IntegrityError, models
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from catalog.models import Item, Tag
from .forms import EditProfileForm, LoginForm, RegisterForm
from .models import Profile

USER_LIST_TEMPLATE = 'users/user_list.html'
CUR_USER_TEMPLATE = 'users/user_detail.html'
SIGNUP_TEMPLATE = 'users/signup.html'
LOGIN_TEMPLATE = 'users/login.html'
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


def login_view(request) -> HttpResponse:
    """
    Возвращает страничку регистрации пользователя
    """

    if request.user.is_authenticated:
        return redirect('/auth/profile', status=HTTPStatus.OK,
                        context={}, content_type='text/html')

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(
                    '/auth/profile', status=HTTPStatus.OK,
                    context={},
                    content_type='text/html')
    form = LoginForm()
    return render(
        request, LOGIN_TEMPLATE, status=HTTPStatus.OK,
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
        request, LOGIN_TEMPLATE, status=HTTPStatus.OK,
        context={"form_login": form_login},
        content_type='text/html'
    )


def signup(request) -> HttpResponse:
    errors = []

    if request.user.is_authenticated:
        logout(request)

    form = RegisterForm(request.POST or None)

    if form.is_valid():

        username = form.cleaned_data['username']
        password1 = form.cleaned_data['password1']

        if not errors:
            try:

                new_user = User(
                    username=username,
                    password=make_password(password1),
                )
                new_user.save()

                new_user.save()
                Profile.objects.create(user=new_user)
                new_user.profile.save()

                login(request, new_user)

                return redirect('/auth/profile', status=HTTPStatus.OK,
                                context={}, content_type='text/html')

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


def profile(request) -> HttpResponse:
    """
    Возвращает страничку профиля пользователя
    """

    user = request.user
    # if user.email is not None:
    #     send_mail("Тест", 'Тест', 'admin@example.com', [user.email],
    #               fail_silently=False)

    if not user.is_authenticated:
        return redirect('login',
                        context={}, content_type='text/html')
    errors = []

    if request.POST:
        form = EditProfileForm(request.POST)

        if form.is_valid():

            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.profile.birthday = form.cleaned_data['birthday']

            email = form.cleaned_data['email']

            if User.objects.filter(email=email):
                errors.append('Пользователь с этой почтой уже есть')

            if not errors:
                user.email = email
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
