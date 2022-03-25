from lib2to3.pgen2 import token
from turtle import st
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

#------------------------------Тестирование регистрации пользователя------------------------------#

class RegistrationTestCase(APITestCase):

    def test_registration(self):

        data = {"username":"Ivan2","email":"ivan@localhost.app", "password":"12345"}
        response = self.client.post("/api/v1/registration/", data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

#------------------------------Тестирование модели книг(CRUD)------------------------------#

class OperationWitchBooksTestCase(APITestCase):

    def setUp(self): # Получение access токена get запросом

        data = {"username":"Ivan3","email":"ivan@localhost.app", "password":"12345"}
        response = self.client.post("/api/v1/registration/", data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        data = {
                 "username": "Ivan3",
                 "password": "12345"
               }
        self.access_token = self.client.post("/api/v1/token/",data).data.get("access")
        self.client.credentials(HTTP_AUTHORIZATION = f'JWT {self.access_token}')

    #-------Создание----------#

    def test_create_book(self):

        data_autor = {"name":"Fedya","surname":"Stafeev","date_birth":"2004-02-17"}
        temp = self.client.post("/api/v1/read_and_create_autor/",data_autor)

        data_book = {
                
                "title":"Книга",
                "description":"ОписаниеКниги",
                "autor": 1
               }
        response = self.client.post('/api/v1/read_and_create_book/',data_book)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    #-------Чтение----------#

    def test_read_book(self):
        
        response = self.client.get("/api/v1/read_and_create_book/")
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    #-------Редактирование----------#

    def test_update_book(self):

        data_autor = {"name":"Fedya","surname":"Stafeev","date_birth":"2004-02-17"}
        response = self.client.post("/api/v1/read_and_create_autor/",data_autor)

        data_book = {
                "title":"Книга",
                "description":"ОписаниеКниги",
                "autor": 1
               }
        response = self.client.post('/api/v1/read_and_create_book/',data_book)

        data = {
                "title":"КнигаИзменить",
                "description":"ОписаниеКнигиИзменилось",
                "autor": 1
               }
        response = self.client.put('/api/v1/update_book/1/',data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #-------Удаление----------#

    def test_delete_book(self):
                        
        data_autor = {"name":"Fedya","surname":"Stafeev","date_birth":"2004-02-17"}
        response = self.client.post("/api/v1/read_and_create_autor/",data_autor)

        data_book = {
                "title":"Книга",
                "description":"ОписаниеКниги",
                "autor": 1
               }
        response = self.client.post('/api/v1/read_and_create_book/',data_book)

        response = self.client.delete("/api/v1/delete_book/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


#------------------------------Тестирование получения access токена------------------------------#

class GetAccessTokenTestCase(APITestCase):

    def test_get_access_token(self):
        data = {"username":"Ivan2","email":"ivan@localhost.app", "password":"12345"}
        response = self.client.post("/api/v1/registration/", data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        data = {
                 "username": "Ivan2",
                 "password": "12345"
               }
        response = self.client.post("/api/v1/token/",data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)


#------------------------------Тестирование модели авторов(CRUD)------------------------------#

class OperationWitchAutorsTestCase(APITestCase):

    def setUp(self):
        data = {"username":"Ivan2","email":"ivan@localhost.app", "password":"12345"}
        response = self.client.post("/api/v1/registration/", data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        data = {
                 "username": "Ivan2",
                 "password": "12345"
               }
        self.access_token = self.client.post("/api/v1/token/",data).data.get("access")
        self.client.credentials(HTTP_AUTHORIZATION = f'JWT {self.access_token}')

    def test_create_autor(self):

        data = {"name":"Fedya","surname":"Stafeev","date_birth":"2004-02-17"}
        response = self.client.post("/api/v1/read_and_create_autor/",data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_read_autors(self):
        response = self.client.get('/api/v1/read_and_create_autor/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_update_autor(self):

        data = {"name":"Fedya","surname":"Stafeev","date_birth":"2004-02-17"}
        response = self.client.post("/api/v1/read_and_create_autor/",data)

        data = {
                "name": "Иван2",
                "surname": "Горшунов",
                "patronymic": "Алексеевич",
                "date_birth": "2004-02-12"
                }
        response = self.client.put('/api/v1/update_autor/1/',data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_delete_autor(self):
        data = {"name":"Fedya","surname":"Stafeev","date_birth":"2004-02-17"}
        temp = self.client.post("/api/v1/read_and_create_autor/",data)
        response = self.client.delete('/api/v1/delete_autor/1/')
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    

    