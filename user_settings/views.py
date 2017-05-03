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
from .serializers import UserDetailSerializer, ProfileSerializer

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
            reply['data'] = UserDetailSerializer(users, many=True).data
        except:
            reply['data']=[]
        return Response(reply, status.HTTP_200_OK)


class UserProfile(APIView):
    serializer_class = UserDetailSerializer
    def get(self, request, token=None, format=None):
        """
        Returns a list of profile of user
        """
        reply={}
        print('request', request.user)
        try:
            # user_instance = User.objects.filter(user=request.user)
            if token:
                user = User.objects.get(id=token)
                reply['data'] = self.serializer_class(user).data
            else:
                reply['data'] = self.serializer_class(user_instance, many=True).data
        except User.DoesNotExist:
            return error.RequestedResourceNotFound().as_response()
        except:
            return error.UnknownError().as_response()
        # except:
        #     reply['data']=[]
        return Response(reply, status.HTTP_200_OK)

    def put(self, request, token=None, *args, **kwargs):
        """
        update a profile
        """
        if token:
            try:
                user = User.objects.get(id=token)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        serialized_data = self.serializer_class(instance=user, data=request.data, partial=True)
        reply={}
        if serialized_data.is_valid():
            # print('valid', serialized_data)
            user = serialized_data.save()
            reply['data'] = self.serializer_class(instance=user, many=False).data
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


# class LoginView(views.APIView):
#     def post(self, request, format=None):
#         data = json.loads(request.body)
#
#         email = data.get('email', None)
#         password = data.get('password', None)
#
#         account = authenticate(email=email, password=password)
#
#         if account is not None:
#             if account.is_active:
#                 login(request, account)
#
#                 serialized = UserDetailSerializer(account)
#
#                 return Response(serialized.data)
#             else:
#                 return Response({
#                     'status': 'Unauthorized',
#                     'message': 'This account has been disabled.'
#                 }, status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             return Response({
#                 'status': 'Unauthorized',
#                 'message': 'Username/password combination invalid.'
#             }, status=status.HTTP_401_UNAUTHORIZED)
