# Standard Library
import requests


def connector(*, url: str) -> str:
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    return response
