# Libreries
import pytest

# Django
from django.test import TestCase

# Internal
from math_challenge.math_challenge import (
  least_common_multiple, 
  plus_one
)

def test_least_common_multiple():
  numbers = [2, 3, 5, 7, 11]
  lcm = least_common_multiple(
    numbers=numbers
  )
  expectation = 2310
  assert lcm == expectation

def test_plus_one():
  number = 5
  number_plus_one = plus_one(
    number=number
  )
  expectation = 6
  assert number_plus_one == expectation
