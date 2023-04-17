from rest_framework.test import APITestCase


class TestJokeChallengeViews(APITestCase):    
    def test_post_valid_data(self):
        valid_input_data = {"text": "joke"}
        response = self.client.post("/joke_challenge/joke/", data=valid_input_data, format="json")
        self.assertEqual(response.status_code, 200)     
