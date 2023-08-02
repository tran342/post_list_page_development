from django.contrib.auth.backends import UserModel
from django.contrib.auth.models import User
from django.core.management import BaseCommand

from models.author.factories import AuthorFactory
from models.author.models import Author
from models.comment.factories import CommentFactory
from models.comment.models import Comment
from models.post.factories import PostFactory
from models.post.models import Post


class Command(BaseCommand):
    help = "Feed fake data to test."

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        username = 'customer@mail.com'
        user = User.objects.filter(username=username).first()
        if not user:
            user = UserModel.objects.create_user(username, first_name='First', last_name='Last')

        Author.objects.all().delete()
        Comment.objects.all().delete()
        Post.objects.all().delete()

        AuthorFactory.create(user=user)
        PostFactory.create_batch(50, author=user.author)

        first_post = Post.valid_objects.all().first()
        CommentFactory.create_batch(5, post=first_post, author=user.author)

        last_post = Post.valid_objects.all().last()
        CommentFactory.create_batch(5, post=last_post, author=user.author)
