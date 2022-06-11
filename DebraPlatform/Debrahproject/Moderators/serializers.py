from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserSettingModel


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'password']

class UserSettingSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserSettingModel
        fields = '__all__'


