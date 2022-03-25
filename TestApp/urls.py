"""TestApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

from TestTaskApp.views import BooksAPIDestroy,BooksAPIList,BooksAPIUpdate,AutorsAPIList,AutorsAPIUpdate,AutorsAPIDestroy,RegistrationUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/login_users/', include('rest_framework.urls')),
    path('accounts/profile/', BooksAPIList.as_view()),
    path('api/v1/read_and_create_book/', BooksAPIList.as_view(),name = 'read_books'),
    path('api/v1/update_book/<int:pk>/', BooksAPIUpdate.as_view(),name = 'update_books'),
    path('api/v1/delete_book/<int:pk>/', BooksAPIDestroy.as_view(),name = 'delete_books'),
    path('api/v1/read_and_create_autor/', AutorsAPIList.as_view(),name = 'read_autors'),
    path('api/v1/update_autor/<int:pk>/', AutorsAPIUpdate.as_view(),name = 'update_autors'),
    path('api/v1/delete_autor/<int:pk>/', AutorsAPIDestroy.as_view(),name = 'delete_autors'),
    path('api/v1/registration/', RegistrationUserView.as_view(),name = 'registration') ,
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

