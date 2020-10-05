import factory
from surveys.models import Survey


class SurveyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Survey
    title = factory.Faker('catch_phrase')
    description = factory.Faker('text')
