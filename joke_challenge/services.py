# Standard Library
from datetime import datetime
from typing import Union

# Django
from django.db import transaction

from joke_challenge.constants import options
# Internal
from joke_challenge.joke_challenge import get_chuck_joke, get_random_joke
from joke_challenge.models import Joke


def services_get_joke(
    *,
    param: str
) -> str:
    response = {}
    if param:
        if param.lower() == options.CHUCK.value:
            response["response"] = get_chuck_joke()
            return response
        elif param.lower() == options.DAD.value:
            response["response"] = get_random_joke()
            return response
        else:
            response["response"] = options.INVALID.value
            return response
    else:
        response["response"] = get_chuck_joke()
        return response


@transaction.atomic()
def services_save_joke(
    *,
    text: str
) -> Union[None, None]:
    Joke(
        create_at=datetime.now(),
        update_at=datetime.now(),
        joke=text,
        is_active=True,
    ).save()


@transaction.atomic()
def services_update_joke(
    *,
    text: str,
    number: int
)-> Union[None, None]:
    joke = Joke.objects.get(
        pk=number
    )
    joke.joke = text
    joke.save()


@transaction.atomic()
def services_delete_joke(
    *,
    number: int
)-> Union[None, None]:
    joke = Joke.objects.get(
        pk=number
    )
    joke.delete()
