from rest_framework import serializers

from django.contrib.auth.models import User

from user_settings.models import Profile, ProfileImage

class ProfileSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedRelatedField(source="user", view_name="user_profile")
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Profile
        fields = ('token', 'user','current_location', 'permanent_location', 'dob',
                    'about_me', 'gender_status', 'create_profile_for', 'marital_status',
                    'height', 'weight', 'body_type', 'complexion',)

    def to_internal_value(self, data):
        first_name = data.pop('first_name', None)
        last_name = data.pop('last_name', None)
        data = super(ProfileSerializer, self).to_internal_value(data)
        print('data', data)
        data['first_name'] = first_name
        data['last_name'] = last_name
        return data

    def update(self, instance, validated_data):
        first_name = validated_data.pop('first_name', None)
        last_name = validated_data.pop('last_name', None)
        user_inst_fields = {}
        if first_name:
            user_inst_fields['first_name'] = first_name
        if last_name:
            user_inst_fields['last_name'] = last_name
        if user_inst_fields:
            User.objects.update_or_create(id=instance.user.id, defaults=user_inst_fields)
        profile, created = Profile.objects.update_or_create(token=instance.token, defaults=validated_data)
        print('profile', profile, created)
        return profile

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)
    class Meta:
        model = User
        fields = ('id', 'profile', 'username', 'email', 'first_name', 'last_name',)

    # def update(self, instance, validated_data):
    #     # instance = super(UserSerializer, self).update(validated_data)
    #     profile_data = validated_data.pop('profile')
    #     #updating user data
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.email = validated_data.get('first_name', instance.email)
    #     #updating profile data
    #     if not instance.profile:
    #         Profile.objects.create(user=instance, **profile_data)
    #     instance.profile.current_location = profile_data.get('current_location', instance.profile.current_location)
    #     instance.profile.permanent_location = profile_data.get('permanent_location', instance.profile.permanent_location)
    #     instance.profile.weight = profile_data.get('weight', instance.profile.weight)
    #     instance.profile.height = profile_data.get('height', instance.profile.height)
    #     instance.profile.about_me = profile_data.get('about_me', instance.profile.about_me)
    #     instance.profile.create_profile_for = profile_data.get('create_profile_for', instance.profile.create_profile_for)
    #     instance.profile.body_type = profile_data.get('body_type', instance.profile.body_type)
    #     instance.save()
    #     return instance
