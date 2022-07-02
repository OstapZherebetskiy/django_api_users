from django.test import TestCase
from rest_framework.test import APIClient
from .models import Post
from django.contrib.auth.models import User

# Create your tests here.


class APITest(TestCase):
    def test_post_get_by_id(self):
        self.user = User.objects.create_user(
            email='test@gmail.com', password='test1test', username='test')

        client = APIClient()
        client.force_authenticate(user=self.user)

        post = Post(title='Test', text='Test', user=self.user)
        post.save()

        response = client.get('http://127.0.0.1:8000/post/1/', format='json')
        self.assertEqual(response.status_code, 200)
        print('test-1: PASS')

    def test_post_update(self):
        self.user = User.objects.create_user(
            email='test@gmail.com', password='test1test', username='test')

        client = APIClient()
        client.force_authenticate(user=self.user)

        post = Post(title='Test', text='Test', user=self.user)
        post.save()

        response = client.put(
            'http://127.0.0.1:8000/post/1/',  data={'title': 'testttt', 'text': 'test textttt'})
        self.assertEqual(response.status_code, 200)
        print('test-2: PASS')

    def test_posts_get(self):

        self.user = User.objects.create_user(
            email='test@gmail.com', password='test1test', username='test')

        client = APIClient()
        client.force_authenticate(user=self.user)

        response = client.get('http://127.0.0.1:8000/post/', format='json')
        self.assertEqual(response.status_code, 200)
        print('test-3: PASS')

    def test_register(self):
        response = self.client.post('http://127.0.0.1:8000/register/', {
                                    'username': 'testuser', 'password': '123test123', 'password2': '123test123'})
        self.assertEqual(response.status_code, 201)
        print('test-4: PASS')
