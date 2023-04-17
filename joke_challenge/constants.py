# Standard Library
from enum import Enum

from decouple import config


class urls(Enum):
    ICANHAZDADJOKE = config('URL_ICANHAZDADJOKE')
    CHUCKNORRIS = config('URL_CHUCKNORRIS')

class options(Enum):
    CHUCK = "chuck"
    DAD = "dad"
    INVALID = "param no vàlido, asegurese que sea chuck ó Dad"
