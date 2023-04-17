# Internal
from math_challenge.math_challenge import (
    least_common_multiple, 
    plus_one
)


def services_least_common_multiple(
    *,
    numbers: list
) -> list:
    response = least_common_multiple(
        numbers=numbers
    )
    return {"response": response}
    

def services_plus_one(
    *,
    number: int
) -> int:
    response = plus_one(
        number=number
    )
    return {"response": response}
