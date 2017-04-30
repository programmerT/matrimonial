from django.conf import settings
from django import forms

from user_settings.models import Profile

PROFILE_CHOICE = [
    (0, 'Self'),
    (1, 'Son'),
    (2, 'Daughter'),
    (3, 'Relatives'),
]

class SignupForm(forms.Form):
    # create_profile_for = forms.ChoiceField(choices=PROFILE_CHOICE)

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['create_profile_for'] = forms.ChoiceField(choices=PROFILE_CHOICE)

    def signup(self, request, user):
        user.save()
        profile = Profile()
        profile.user_id = user.id
        profile.create_profile_for = self.cleaned_data.get('create_profile_for')
        profile.save()
