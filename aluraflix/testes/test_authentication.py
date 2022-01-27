from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse


class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('programas-list')
        self.user = User.objects.create_user('test', password='123465')

    def test_atentica_credenciais(self):
        """Verifica a autenticação de um usuario"""

        user = authenticate(username='test', password='123465')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_autenticacao(self):
        """Teste para verificar se o usuario errar o login"""

        user = authenticate(username='test2', password='123465')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_get_sem_autorizacao(self):
        """Teste para verificar uma chamada GET sem se autenticar"""

        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_com_autenticacao(self):
        """Teste par averificar uma chamada GET com autenticação correta"""

        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
