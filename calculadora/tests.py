from django.test import TestCase

from .calculator import Calculator


class CalculatorTestCase(TestCase):
    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(2, 3), 5)

    def test_subtract(self):

        calc = Calculator()
        self.assertEqual(calc.subtract(5, 3), 2)

    def test_multiply(self):
        calc = Calculator()
        self.assertEqual (calc.multiply(4, 3), 12)
    
    def test_divide(self):
        calc = Calculator()
        self.assertEqual(calc.divide(10, 2), 5)

    def test_divide_by_zero(self):
        calc = Calculator()
        with self,assertRaises(ValueError):
            calc.divide(10, 0)