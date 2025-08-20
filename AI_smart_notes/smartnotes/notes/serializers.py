from rest_framework import serializers
from .models import Note, Reminder
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Note
        fields = "__all__"

class ReminderSerializer(serializers.ModelSerializer):  
    class Meta:
        model  = Reminder
        fields = "__all__"

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)        
                