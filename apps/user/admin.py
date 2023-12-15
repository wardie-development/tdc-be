from django.contrib import admin
from django.contrib.auth.models import Group


# unregister the Group model from admin.

admin.site.unregister(Group)
