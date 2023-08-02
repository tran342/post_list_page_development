import factory
from factory import SubFactory
from factory.fuzzy import FuzzyText


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'model_post.Post'

    title = FuzzyText()
    content = FuzzyText()
    author = SubFactory('model_author.AuthorFactory')
