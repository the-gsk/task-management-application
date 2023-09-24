from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
from rest_framework import serializers

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.

    Allows the creation of new user accounts.
    """

    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Create a new user account.

        Args:
            validated_data (dict): Validated data containing username and password.

        Returns:
            User: The newly created user instance.
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for tasks.

    Provides serialization and deserialization of task data.
    """

    class Meta:
        model = Task
        fields = '__all__'
