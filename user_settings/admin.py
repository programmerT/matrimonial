# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib import admin

from .models import Profile, ProfileImage

class ProfileInline(admin.StackedInline):
    model = Profile

class ProfileImageInline(admin.StackedInline):
    model = ProfileImage

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# admin.site.register(Profile)
admin.site.register(ProfileImage)
