from typing import Union
from unittest import TestCase

# Function code
def divide(dividend: Union[int, float], divisor: Union[int, float]):
    if divisor == 0:
        raise ValueError("Divisor Cannot Be Zero")
    return dividend/divisor


# test Function Code

class TestFunctions(TestCase):
    def test_divide_result(self):
        dividend = 15
        divisor = 3
        expected_result = 5.0
        self.assertAlmostEqual(divide(dividend, divisor), expected_result)

    def test_divide_by_negative(self):
        dividend = 15
        divisor = -3
        expected_result = -5.0
        self.assertAlmostEqual(divide(dividend,divisor), expected_result)


    def test_divide_by_zero(self):
        dividend = 0
        divisor =  5
        expected_result = 0
        self.assertAlmostEqual(divide(dividend, divisor), expected_result)


    def test_divide_error_on_zero(self):
        with self.assertRaises(ValueError):
            divide(25, 0)