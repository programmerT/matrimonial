from django.conf.urls import include, url

from . import views
# from api.views import user_list

urlpatterns = [
    url(
        r'^basic_profile/$',
        views.BasicProfileUpdateView.as_view(),
        name='profile_update'
    ),
    url(
        r'^users/$',
        views.UserList.as_view(),
        name="user_list"
    ),
    # url(
    #     r'^users/(?P<token>[0-9a-z]+)$',
    #     views.UserList.as_view(),
    #     name="user_profile"
    # ),
    url(
        r'^user/profile/(?P<token>[0-9a-z]+)?$',
        views.UserProfile.as_view(),
        name="user_profile"
    )
]
