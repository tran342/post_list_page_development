import factory
from factory.fuzzy import FuzzyText


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'model_author.Author'

    nickname = FuzzyText()
