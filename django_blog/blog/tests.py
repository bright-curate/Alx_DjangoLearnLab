from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class PostViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='pass1234')
        self.other = User.objects.create_user(username='other', password='pass1234')

        self.post = Post.objects.create(
            title='Test Post',
            content='Test content',
            author=self.user
        )

    def test_list_view(self):
        url = reverse('posts-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_detail_view(self):
        url = reverse('post-detail', kwargs={'pk': self.post.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)

    def test_create_requires_login(self):
        url = reverse('post-create')
        response = self.client.get(url)
        # should redirect to login
        self.assertNotEqual(response.status_code, 200)

        self.client.login(username='tester', password='pass1234')
        response = self.client.post(url, {'title': 'New', 'content': 'New content'})
        self.assertEqual(response.status_code, 302)  # redirect to detail

    def test_edit_only_author(self):
        url = reverse('post-edit', kwargs={'pk': self.post.pk})
        # other user cannot edit
        self.client.login(username='other', password='pass1234')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)  # UserPassesTestMixin returns 403

    def test_delete_only_author(self):
        url = reverse('post-delete', kwargs={'pk': self.post.pk})
        self.client.login(username='tester', password='pass1234')
        response = self.client.post(url)
        # after delete should redirect to posts list
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())

