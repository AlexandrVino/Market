from django.contrib.auth import get_user_model
from django.db.models import Prefetch
from .models import Profile
from datetime import datetime

User = get_user_model()


def users_birthday(request):
    cur_date = str(datetime.date(datetime.now()))[5:]
    return {
        "birthday_list": Profile.objects.filter(birthday__contains=cur_date).prefetch_related(
            Prefetch(
                "user",
                queryset=User.objects.all(),
            ),
        )
    }
