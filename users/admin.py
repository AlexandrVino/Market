from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import Profile

User = get_user_model()


class ProfileInlined(admin.TabularInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInlined,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
