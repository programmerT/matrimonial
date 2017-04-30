from django.contrib.auth.models import User
from django import forms

from django.core.exceptions import ValidationError
from multiupload.fields import MultiImageField

from .models import Profile, ProfileImage
from .choices import *

class BasicProfileUpdateForm(forms.ModelForm):
    # gender_choice = [('','Gender'), ('M','Male'), ('F','Female')]
    dob = forms.DateField()
    gender = forms.ChoiceField(choices=gender_choice,
    	widget=forms.Select(attrs={'class': 'ui search dropdown'}))
    first_name = forms.CharField(label="First Name", max_length=120)
    last_name = forms.CharField(label="Last Name", max_length=120)
    marital_status = forms.ChoiceField(choices = marital_status_choice,
    	widget=forms.Select(attrs={'class': 'ui search dropdown'}))
    contact_no = forms.IntegerField(widget=forms.TextInput(
            attrs={'placeholder': 'Please provide contact number where one can get in touch with proposal'}
            ))
    reason_registration = forms.ChoiceField(choices = reason_registration_choice,
    	widget=forms.Select(attrs={'class': 'ui search dropdown'}))

    class Meta:
        model = Profile
        fields = [
        'dob'
        ,'gender'
        ,'current_location'
        ,'permanent_location'
        ,'marital_status'
        ,'reason_registration'
        ,'contact_no'
        ]

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            # name = kwargs['instance'].name
            # kwargs.setdefault('initial', {})['confirm_email'] = email
            # dob'].widget.format = '%d/%m/%Y'
            widgets = {
             'dob': forms.DateInput(attrs={'class':'myDateClass',
                                             'placeholder':'Select a date'})
        	}
        super(BasicProfileUpdateForm, self).__init__(*args, **kwargs)
        try:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
        except User.DoesNotExist:
            pass


    def save(self, *args, **kwargs):
        user_instance = self.instance.user
        user_instance.first_name = self.cleaned_data.get('first_name')
        user_instance.last_name = self.cleaned_data.get('last_name')
        user_instance.save()
        profile = super(BasicProfileUpdateForm, self).save(*args, **kwargs)
        return profile

class AboutMeProfileForm(forms.ModelForm):
    about_me = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Briefy describe about yourself', 'rows':'10'}))
    looking_for = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Please brief your expectation regarding partner', 'rows':'10'}))
    complexion = forms.ChoiceField(choices = complexion_choice,
        widget=forms.Select(attrs={'class': 'ui search dropdown'}))
    body_type = forms.ChoiceField(choices = body_type_choice,
        widget=forms.Select(attrs={'class': 'ui search dropdown'}))
    height = forms.ChoiceField(choices = height_choice,
        widget=forms.Select(attrs={'class': 'ui search dropdown'}))
    weight = forms.ChoiceField(choices = weight_choice,
        widget=forms.Select(attrs={'class': 'ui search dropdown'}))

    class Meta:
        model = Profile
        fields = [
        'height',
        'weight',
        'body_type',
        'complexion',
        'about_me',
        'looking_for'
        ]

    def __init__(self, *args, **kwargs):
        super(AboutMeProfileForm, self).__init__(*args, **kwargs)
        # self.fields['height'].widget.attrs['placeholder'] = '5ft 10inch'
        # self.fields['weight'].widget.attrs['placeholder'] = '65 kgs'

class QualificationWorkProfileForm(forms.ModelForm):
    qualification = forms.ChoiceField(choices = qualification_choice,
        widget=forms.Select(attrs={'class': 'ui search dropdown'}))
    occupation = forms.ChoiceField(choices = occupation_choice,
        widget=forms.Select(attrs={'class': 'ui search dropdown'}))
    income = forms.ChoiceField(choices = income_choice,
        widget=forms.Select(attrs={'class': 'ui search dropdown'}))

    class Meta:
        model = Profile
        fields = [
        'qualification'
        ,'occupation'
        ,'income'
        ]

    # def __init__(self, *args, **kwargs):

    #     if kwargs.get('instance'):
    #         name = kwargs['instance'].name
    #         # self.fields['about_me'].widget.attrs = { 'placeholder':'About me', 'rows':'10'}
    #         # self.fields['looking_for'].widget.attrs = { 'placeholder':'What I Am Looking For?', 'rows':'10'}


    #     return super(QualificationWorkProfileForm, self).__init__(*args, **kwargs)

class ReligionProfileForm(forms.ModelForm):
    cast = forms.CharField()

    class Meta:
        model = Profile
        fields = [
        'cast',
        'is_inter_cast',
        ]

    # def __init__(self, *args, **kwargs):

    #     if kwargs.get('instance'):
    #         name = kwargs['instance'].name

    #     return super(UserReligionInformationForm, self).__init__(*args, **kwargs)

class ProfileImageUploadForm(forms.Form):
    # For images (requires Pillow for validation 2MB):
    profile_image = MultiImageField(min_num=1, max_num=3, max_file_size=1024*1024*2, required=False)

    class Meta:
        model = ProfileImage

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            instance = ProfileImage.objects.filter(user_id=self.request.user.id)

        return super(ProfileImageUploadForm, self).__init__(*args, **kwargs)

class FamilyProfileForm(forms.ModelForm):
    father_name = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': 'Father/Guardian Name'}
            ))
    mother_name = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': 'Mother/Sister Name'}
            ))

    class Meta:
        model = Profile
        fields = [
        'father_name'
        ,'mother_name'
        ]
