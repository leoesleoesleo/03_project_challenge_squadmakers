# Standard Library
from joke_challenge import connector
from joke_challenge.constants import urls


def get_random_joke() -> str:
    """
    If no path param is passed or the param is "Dad"
    Function that consumes the icanhazdadjoke API 
    and returns a random joke.
    """
    url = urls.ICANHAZDADJOKE.value
    response = connector.connector(url=url)
    json_data = response.json()
    return json_data['joke']


def get_chuck_joke() -> str:
    """
    Function that consumes the chucknorris API and 
    returns a random joke of
    Chuck Norris.
    """
    url = urls.CHUCKNORRIS.value
    response = connector.connector(url=url)
    json_data = response.json()
    return json_data['value']
