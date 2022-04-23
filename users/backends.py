from django.contrib.auth import get_user_model, login

from users.models import Profile

User = get_user_model()


class EmailUniqueFailed(BaseException):
    def __str__(self):
        return 'Пользователь с этой почтой уже есть'


class EmailAuthBackend:
    @staticmethod
    def authenticate(request, email=None, password=None):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                login(request, user)
                return user
            return None
        except User.DoesNotExist:
            return None

    @staticmethod
    def create_user(email=None, username=None, password1=None, password2=None):
        """ Create a new user profile """

        if not email:
            raise ValueError('User must have an email address')

        if User.objects.filter(email=email):
            raise EmailUniqueFailed()

        user = User(email=email, username=username)
        user.set_password(password1)
        user.is_active = False
        user.save()
        Profile.objects.create(user=user)
        user.profile.save()

        return user

    @staticmethod
    def get_user(user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
