from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from apps.user.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass


admin.site.unregister(Group)
