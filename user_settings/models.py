# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
import string

from django.utils.translation import ugettext_lazy as _
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models

from .choices import (
        gender_choice, marital_status_choice, height_choice, weight_choice, reason_registration_choice,
        income_choice, occupation_choice, qualification_choice, body_type_choice, complexion_choice, profile_choice,
    )


def token_generator():
    return ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(9))

class Profile(models.Model):
    token = models.CharField(default=token_generator, max_length=20, unique=True, editable=False)
    user = models.OneToOneField(User)
    current_location = models.CharField(_('Current Location'), blank=True, max_length=200)
    permanent_location = models.CharField(_('Permanent Location'), blank=True, max_length=200)
    dob = models.DateField(_('Date of Birth'), null=True)
    about_me = models.TextField(null=True)
    gender_status = models.CharField(choices=gender_choice, default="M", null=True, max_length=1)
    create_profile_for = models.IntegerField(choices=profile_choice, default=0, null=True)
    marital_status = models.IntegerField(choices=marital_status_choice, null=True)
    height = models.IntegerField(choices=height_choice, null=True)
    weight = models.IntegerField(choices=weight_choice, null=True)
    body_type = models.IntegerField(choices=body_type_choice, null=True)
    complexion = models.IntegerField(choices=complexion_choice, null=True)
    reason_registration = models.IntegerField(choices=reason_registration_choice, null=True)
    is_inter_cast = models.BooleanField(default=True)
    #Qualification and Work
    qualification = models.IntegerField(choices=qualification_choice, null=True)
    occupation = models.IntegerField(choices=occupation_choice, null=True)
    income = models.IntegerField(choices=income_choice, null=True)
    #Cast
    cast = models.CharField(_('Cast'), max_length=120, blank=True)
    #Family Background
    father_name = models.CharField(_('Father name'),
        blank=True,
        max_length=255)
    mother_name = models.CharField(_('Mother name'),
        blank=True,
        max_length=255)
    contact_no = models.CharField(
        blank=True,
        max_length=15)


class ProfileImage(models.Model):
    profile_image = models.FileField(upload_to='profile_images', blank=True, null=True)
    profile = models.ForeignKey(Profile, related_name="user_profile")
