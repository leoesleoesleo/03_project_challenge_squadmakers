import unittest
from unittest.mock import patch
from joke_challenge.services import services_get_joke
from joke_challenge.constants import options
import re

class TestServicesGetJoke(unittest.TestCase):
    @patch('joke_challenge.joke_challenge.get_chuck_joke')
    def test_services_get_joke_chuck(
        self,
        mock_get_chuck_joke
    ):
        result = services_get_joke(param='chuck')
        assert type(result["response"]) == str

    @patch('joke_challenge.joke_challenge.get_random_joke')
    def test_services_get_joke_dad(
        self, 
        mock_get_random_joke
    ):
        result = services_get_joke(param='dad')
        assert type(result["response"]) == str

    def test_services_get_joke_invalid_param(self):
        result = services_get_joke(
            param='invalid'
        )
        assert result["response"] == options.INVALID.value

    @patch('joke_challenge.joke_challenge.get_chuck_joke')
    def test_services_get_joke_no_param(
        self, 
        mock_get_chuck_joke
    ):
        result = services_get_joke(param='')        
        assert re.search(
            r"norris", result["response"].lower(), re.IGNORECASE
        )
