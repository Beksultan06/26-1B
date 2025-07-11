from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", 'username', 'email', 'password')

    def create(self, velidated_data):
        user = User.objects.create_user(
            username=velidated_data['username'],
            email=velidated_data['email'],
            password=velidated_data['password']
        )
        return user