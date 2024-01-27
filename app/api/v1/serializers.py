from rest_framework import serializers

from app.models import UserPasswordManager


class UserPasswordManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPasswordManager
        fields = "__all__"
