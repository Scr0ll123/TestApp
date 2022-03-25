from xmlrpc.client import ResponseError
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsNotAuthenticated
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from .models import Books, Autors
from .serializers import BookSerializer, UserSerializer,AutorSerializer


# -------------------Модель Книг----------------#

class BooksAPIList(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class BooksAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, )


class BooksAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, )

# -------------------Модель Авторов----------------#

class AutorsAPIList(generics.ListCreateAPIView):
    queryset = Autors.objects.all()
    serializer_class = AutorSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class AutorsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Autors.objects.all()
    serializer_class = AutorSerializer
    permission_classes = (IsAuthenticated, )


class AutorsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Autors.objects.all()
    serializer_class = AutorSerializer
    permission_classes = (IsAuthenticated, )
    

# -------------------Окно регистрации----------------#

class RegistrationUserView(CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
    permission_classes = (IsNotAuthenticated, )
        

