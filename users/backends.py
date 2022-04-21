from django.contrib.auth import get_user_model, login

User = get_user_model()


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
    def get_user(user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
