from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment

class CommentTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='pass1234')
        self.other = User.objects.create_user(username='user2', password='pass1234')
        self.post = Post.objects.create(title='P', content='C', author=self.user)

    def test_create_comment_requires_auth(self):
        url = reverse('comment-create', kwargs={'post_id': self.post.pk})
        response = self.client.post(url, {'content': 'Hello'})
        self.assertEqual(response.status_code, 302)  # redirected to login

        self.client.login(username='user2', password='pass1234')
        response2 = self.client.post(url, {'content': 'Hello'}, follow=True)
        self.assertEqual(response2.status_code, 200)
        self.assertContains(response2, 'Hello')
        self.assertEqual(Comment.objects.count(), 1)

    def test_edit_comment_only_author(self):
        # create comment by other user
        comment = Comment.objects.create(post=self.post, author=self.other, content='Hi')
        url = reverse('comment-edit', kwargs={'pk': comment.pk})
        self.client.login(username='user1', password='pass1234')  # not the author
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)  # forbidden

        # author can access
        self.client.login(username='user2', password='pass1234')
        response2 = self.client.get(url)
        self.assertEqual(response2.status_code, 200)

    def test_delete_comment_only_author(self):
        comment = Comment.objects.create(post=self.post, author=self.other, content='Hi')
        url = reverse('comment-delete', kwargs={'pk': comment.pk})
        self.client.login(username='user1', password='pass1234')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 403)

        self.client.login(username='user2', password='pass1234')
        response2 = self.client.post(url, follow=True)
        self.assertEqual(response2.status_code, 200)
        self.assertFalse(Comment.objects.filter(pk=comment.pk).exists())
