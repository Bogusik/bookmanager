from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


class UserModelTest(TestCase):
    fixtures = ['users.json', 'books.json']

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.get(pk=1)
        self.create_test_data = {
            'author': 'Author',
            'title': 'Book title',
            'description': 'Book description',
        }
        self.update_test_data = {
            'author': 'New author',
            'title': 'New book title',
            'description': 'New book description',
        }

    def test_create_with_authenticated_user(self) -> None:
        self.client.login(username=self.user.username, password='qwe123qwe')

        response = self.client.post('/api/books/', data=self.create_test_data)

        self.assertEqual(response.status_code, 201)

    def test_create_with_not_authenticated_user(self) -> None:

        response = self.client.post('/api/books/', data=self.create_test_data)

        self.assertEqual(response.status_code, 403)

    def test_list(self) -> None:
        response = self.client.get('/api/books/')

        self.assertEqual(response.status_code, 403)

        self.client.login(username=self.user.username, password='qwe123qwe')

        response = self.client.get('/api/books/')

        self.assertEqual(response.status_code, 200)

    def test_partial_update(self) -> None:

        response = self.client.patch(
            '/api/books/1/',
            data=self.update_test_data
        )

        self.assertEqual(response.status_code, 403)

        self.client.login(username=self.user.username, password='qwe123qwe')

        response = self.client.patch(
            '/api/books/1/',
            data=self.update_test_data
        )

        self.assertEqual(response.status_code, 200)

        response = self.client.patch(
            '/api/books/3/',
            data=self.update_test_data
        )

        self.assertEqual(response.status_code, 404)

    def test_destroy(self) -> None:

        response = self.client.delete('/api/books/3/')

        self.assertEqual(response.status_code, 403)

        self.client.login(username=self.user.username, password='qwe123qwe')

        response = self.client.delete('/api/books/3/')

        self.assertEqual(response.status_code, 404)

        response = self.client.delete('/api/books/1/')

        self.assertEqual(response.status_code, 204)
