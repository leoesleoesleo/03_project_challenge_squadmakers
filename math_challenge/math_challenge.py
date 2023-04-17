# Standard Library
from math import gcd
from math_challenge.constants import math


def least_common_multiple(
    *,
    numbers: list
) -> list:
    """
    Function that receives a list of integers
    and returns the least common multiple (LCM) of them.
    """
    # Initialize the LCM with the first number in the list
    lcm = numbers[0]
    # Go through the list of numbers and calculate the LCM
    for num in numbers[1:]:
        lcm = lcm * num // gcd(lcm, num)
    return lcm


def plus_one(
    *,
    number: int
) -> int:
    return number + math.PLUS_ONE.value
