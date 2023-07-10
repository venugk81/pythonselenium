import pytest

@pytest.fixture
def input_value():
   input = ((1,2,3), (1,2,3))
   return input


def test_divisible_by_3(input_value):
   print(input_value)
   print(type(input_value))
   for x in input_value:
       print(x)