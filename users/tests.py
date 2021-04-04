from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


class UserModelTest(TestCase):
    fixtures = ['users.json']

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.get(pk=1)
        self.create_test_data = {
            'email': 'test@test.test',
            'username': 'test',
            'password': 'test',
            'first_name': 'test',
            'last_name': 'test',
        }
        self.update_test_data = {
            'email': 'test@test.test',
            'username': 'test'
        }

    def test_create_with_authenticated_user(self) -> None:
        self.client.login(username=self.user.username, password='qwe123qwe')

        response = self.client.post('/api/users/', data=self.create_test_data)

        self.assertEqual(response.status_code, 403)

    def test_create_with_not_authenticated_user(self) -> None:

        response = self.client.post('/api/users/', data=self.create_test_data)

        self.assertEqual(response.status_code, 201)

    def test_list(self) -> None:
        response = self.client.get('/api/users/')

        self.assertEqual(response.status_code, 403)

        self.client.login(username=self.user.username, password='qwe123qwe')

        response = self.client.get('/api/users/')

        self.assertEqual(response.status_code, 403)

    def test_partial_update(self) -> None:

        response = self.client.patch(
            '/api/users/1/',
            data=self.update_test_data
        )

        self.assertEqual(response.status_code, 403)

        self.client.login(username=self.user.username, password='qwe123qwe')

        response = self.client.patch(
            '/api/users/1/',
            data=self.update_test_data
        )

        self.assertEqual(response.status_code, 200)

        response = self.client.patch(
            '/api/users/2/',
            data=self.update_test_data
        )

        self.assertEqual(response.status_code, 403)

    def test_destroy(self) -> None:

        response = self.client.delete('/api/users/2/')

        self.assertEqual(response.status_code, 403)

        self.client.login(username=self.user.username, password='qwe123qwe')

        response = self.client.delete('/api/users/2/')

        self.assertEqual(response.status_code, 403)

        response = self.client.delete('/api/users/1/')

        self.assertEqual(response.status_code, 204)

    def test_me(self) -> None:

        response = self.client.get('/api/users/me/')

        self.assertEqual(response.status_code, 403)

        self.client.login(username=self.user.username, password='qwe123qwe')

        response = self.client.get('/api/users/me/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.user.username, response.json()['username'])
        self.assertEqual(self.user.id, response.json()['id'])
