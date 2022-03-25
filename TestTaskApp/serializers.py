from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Books,Autors
from rest_framework.validators import UniqueTogetherValidator

UserModel = get_user_model()

class BookSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Books
        fields = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset = model.objects.all(),
                fields=["title"]
            )
         ]

class AutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Autors
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):

    username = serializers.CharField()
    password = serializers.CharField()

   
    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password'],
            email = validated_data['email'],

        )
        user.is_staff = True
        user.save()
        return user
    class Meta:
        model = UserModel
        fields = ("id", "username", "password","email",)
        validators = [
            UniqueTogetherValidator(
                queryset = model.objects.all(),
                fields=["username"]
            ),
            UniqueTogetherValidator(
                queryset = model.objects.all(),
                fields=["email"]
            )
        ]