# Django
from django.test import TestCase

# Internal
from joke_challenge.models import Joke
from joke_challenge.services import (
    services_save_joke,
    services_update_joke,
    services_delete_joke
)


class ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Joke.objects.create(
            id=1,
            joke="test joke",
            is_active=1
        )
        
        Joke.objects.create(
            id=2,
            joke="How do you steal a coat? You jacket.",
            is_active=1
        )
        
    def test_save_joke(self):
        joke = "joke dummy 1"
        services_save_joke(text=joke)
        joke_bd = Joke.objects.filter(
            joke=joke
        ).last()
        assert joke == joke_bd.joke
    
    def test_update_joke(self):
        joke_update = "joke dummy update"    
        id = 1
        services_update_joke(
            text=joke_update,
            number=id
        )
        joke_bd = Joke.objects.filter(
            pk=id
        ).last()
        assert joke_update == joke_bd.joke
    
    def test_delete_joke(self):
        id = 1
        services_delete_joke(
            number=id
        )
        joke_bd = Joke.objects.all()
        cant_joke = len(
            [row.joke for row in joke_bd]
        )
        assert cant_joke == 1
