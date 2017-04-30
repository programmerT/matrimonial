# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, TemplateView, FormView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render


from .models import Profile, ProfileImage
from .forms import ProfileImageUploadForm \
                    ,BasicProfileUpdateForm \
                    ,AboutMeProfileForm \
                    ,QualificationWorkProfileForm \
                    ,ReligionProfileForm \
                    ,FamilyProfileForm
from matrimonial import error


from django.http import HttpResponse, JsonResponse
from .serializers import UserSerializer, ProfileSerializer

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class UserList(APIView):
    # permission_classes = (permissions.IsAuthenticated, )
    def get(self, request, format=None):
        """
        Returns a list of users
        """
        reply={}
        try:
            users = User.objects.all()
            reply['data'] = UserSerializer(users, many=True).data
        except:
            reply['data']=[]
        return Response(reply, status.HTTP_200_OK)


class UserProfile(APIView):
    serializer_class = ProfileSerializer
    def get(self, request, token=None, format=None):
        """
        Returns a list of profile of user
        """
        reply={}
        try:
            profile_instance = Profile.objects.filter(user=self.request.user)
            if token:
                profile = profile_instance.get(token=token)
                reply['data'] = self.serializer_class(profile).data
            else:
                reply['data'] = self.serializer_class(profile_instance, many=True).data
        except:
            reply['data']=[]
        return Response(reply, status.HTTP_200_OK)

    def put(self, request, token=None, *args, **kwargs):
        """
        update a profile
        """
        print('token', token)
        print('request data', request.data)
        if token:
            try:
                profile = Profile.objects.get(token=token)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        serialized_data = self.serializer_class(profile, data=request.data, partial=True)
        reply={}
        if serialized_data.is_valid():
            profile = serialized_data.save(user=request.user)
            reply['data'] = self.serializer_class(profile, many=False).data
            return Response(reply, status.HTTP_200_OK)
        else:
            return Response(serialized_data.errors, status.HTTP_400_BAD_REQUEST)

    # def post(self, request, token=None, format=None):
    #     """
    #     update a profile when token is provided
    #     """
    #     profile=None
    #     print('token', token)
    #     if not token is None:
    #         try:
    #             profile = Profile.objects.get(user=request.user, token=token)
    #         except Profile.DoesNotExist:
    #             return error.RequestedResourceNotFound().as_response()
    #         except:
    #             return error.UnknownError().as_response()
    #     serialized_data = self.serializer_class(profile, data=request.data, partial=True)
    #     reply={}
    #     if not serialized_data.is_valid():
    #         return error.ValidationError(serialized_data.errors).as_response()
    #     else:
    #         profile = serialized_data.save(user=request.user)
    #         reply['data']=self.serializer_class(profile, many=False).data
    #     return Response(reply, status.HTTP_200_OK)


class BasicProfileUpdateView(LoginRequiredMixin, UpdateView):
    # slug_field = 'username'
    # slug_url_kwarg = 'username'
    model = Profile
    template_name = 'user_profile/basic_profile.html'
    form_class = BasicProfileUpdateForm

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('pages:home')

    def get_object(self):
        print('request', self.request.user.id)
        # Only get the User record for the user making the request
        return Profile.objects.get(user=self.request.user.id)
