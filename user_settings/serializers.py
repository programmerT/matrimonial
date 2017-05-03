from rest_framework import serializers

from django.contrib.auth.models import User

from user_settings.models import Profile, ProfileImage

class ProfileSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedRelatedField(source="user", view_name="user_profile")
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    token = serializers.PrimaryKeyRelatedField(read_only=True)
    # first_name = serializers.CharField(source="user.first_name")
    # last_name = serializers.CharField(source="user.last_name")
    # username = serializers.CharField(source="user.username")
    # email = serializers.EmailField(source="user.email")

    class Meta:
        model = Profile
        fields = ('token', 'user', 'current_location', 'permanent_location', 'dob',
                    'about_me', 'gender_status', 'create_profile_for', 'marital_status',
                    'height', 'weight', 'body_type', 'complexion',)

    # def update(self, instance, validated_data):
    #     print('instance', instance.user, instance.user.id)
    #     print('###################################')
    #     first_name = validated_data.pop('first_name', instance.user.first_name)
    #     last_name = validated_data.pop('last_name', instance.user.last_name)
    #     username = validated_data.pop('username', instance.user.username)
    #     print('username', username)
    #     user_inst_fields = {}
    #     if first_name:
    #         user_inst_fields['first_name'] = first_name
    #     if last_name:
    #         user_inst_fields['last_name'] = last_name
    #     if username:
    #         user_inst_fields['username'] = username
    #     if user_inst_fields:
    #         print('instance', instance.user, instance.token)
    #         User.objects.update_or_create(id=instance.user.id, defaults=user_inst_fields)
    #     profile, created = Profile.objects.update_or_create(token=instance.token, defaults=validated_data)
    #     print('profile', profile, created)
    #     return profile

class UserDetailSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    email = serializers.EmailField(source="user.email", read_only=True)
    class Meta:
        model = User
        fields = ('id', 'profile', 'username', 'email', 'first_name', 'last_name',)

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile
        #updating user data
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        #updating profile data
        if not profile:
            Profile.objects.create(user=instance, **profile_data)
        profile.current_location = profile_data.get('current_location', profile.current_location)
        profile.permanent_location = profile_data.get('permanent_location', profile.permanent_location)
        profile.weight = profile_data.get('weight', profile.weight)
        profile.height = profile_data.get('height', profile.height)
        profile.about_me = profile_data.get('about_me', profile.about_me)
        profile.create_profile_for = profile_data.get('create_profile_for', profile.create_profile_for)
        profile.body_type = profile_data.get('body_type', profile.body_type)
        profile.save()
        return instance


    # def update(self, instance, validated_data):
    #     # instance = super(UserSerializer, self).update(validated_data)
    #     profile_data = validated_data.pop('profile')
    #     #updating user data
    #     instance.user.first_name = validated_data.get('first_name', instance.user.first_name)
    #     instance.user.last_name = validated_data.get('last_name', instance.user.last_name)
    #     instance.user.username = validated_data.get('username', instance.user.username)
    #     print('instance', instance.user.username)
    #     instance.user.email = validated_data.get('first_name', instance.user.email)
    #     #updating profile data
    #     if not instance:
    #         Profile.objects.create(user=instance, **profile_data)
    #     instance.current_location = profile_data.get('current_location', instance.current_location)
    #     instance.permanent_location = profile_data.get('permanent_location', instance.permanent_location)
    #     instance.weight = profile_data.get('weight', instance.weight)
    #     instance.height = profile_data.get('height', instance.height)
    #     instance.about_me = profile_data.get('about_me', instance.about_me)
    #     instance.create_profile_for = profile_data.get('create_profile_for', instance.create_profile_for)
    #     instance.body_type = profile_data.get('body_type', instance.body_type)
    #     instance.save()
    #     return instance
