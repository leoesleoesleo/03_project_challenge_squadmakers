# Libreries
import pytest

# Internal
from joke_challenge import connector
from joke_challenge.constants import urls
from joke_challenge.joke_challenge import get_chuck_joke, get_random_joke


def test_get_chuck_joke():
    joke = get_chuck_joke()
    assert type(joke) == str
    assert len(joke) > 0

def test_get_random_joke():
    joke = get_random_joke()
    assert type(joke) == str
    assert len(joke) > 0

def test_status_random_joke():
    url = urls.ICANHAZDADJOKE.value
    response = connector.connector(url=url)
    assert response.status_code == 200

def test_status_chuck_joke():
    url = urls.CHUCKNORRIS.value
    response = connector.connector(url=url)
    assert response.status_code == 200
  