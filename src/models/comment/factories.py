import factory
from factory import SubFactory
from factory.fuzzy import FuzzyText


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'model_comment.Comment'

    content = FuzzyText(length=100)
    post = SubFactory('model_post.PostFactory')
    author = SubFactory('model_author.AuthorFactory')
