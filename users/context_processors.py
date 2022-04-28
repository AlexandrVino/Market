from django.contrib.auth import get_user_model
from django.db.models import Prefetch
from .models import Profile
from django.utils import timezone

User = get_user_model()


def users_birthday(request):
    datetime_now = timezone.now()
    now_day, now_month = datetime_now.day, datetime_now.month
    return {
        "birthday_list": Profile.objects.filter(
            birthday__day=now_day, birthday__month=now_month
        ).prefetch_related(
            Prefetch(
                "user",
                queryset=User.objects.all(),
            ),
        )
    }
