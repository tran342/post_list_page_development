from django.contrib.auth.backends import UserModel
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from models.author.factories import AuthorFactory
from models.comment.factories import CommentFactory
from models.comment.models import Comment
from models.post.factories import PostFactory
from models.post.models import Post


class ListPostTest(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('apis:post:post-list')

        self.data_setup()

    def data_setup(self):
        user_email = 'customer@mail.com'
        self.user = UserModel.objects.create_user(
            user_email, first_name='First', last_name='Last')
        AuthorFactory.create(user=self.user)
        # Create 10 posts
        PostFactory.create_batch(10, author=self.user.author)
        # Only the last post has 10 comments
        post_inst = Post.valid_objects.all().last()
        CommentFactory.create_batch(10, post=post_inst, author=self.user.author)
        self.last_comment_inst = Comment.valid_objects.all().last()

    def test_list(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        resp_content = response.json()['results']
        self.assertEqual(len(resp_content), 10)

        last_comment_content = resp_content[0]['most_recent_comment']
        self.assertIsNotNone(last_comment_content)
        self.assertEqual(last_comment_content, self.last_comment_inst.content)
