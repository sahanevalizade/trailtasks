
import unittest

class Testcalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(-1, 1), 0)


    def  test_subtract(self):
        clac = Calculator()
        self.assertEqual(calc.subtract(5, 3), 2)
        self.assertEqual(calc.subtract(3, 5), -5)


    def test_multiply(self):
        calc = Calculator()
        self.assertEqual(calc.mutiply(4, 3), 12)
        self.assertEqual(calc.multiply(-1, 3), -3)


    def test_divide(self):
        clac = Calculator()
        self.assertEqual(calc.divide(10, 2), 5)
        self.assertEqual(calc.divide(5, 2), 2.5)
    

    with self.assertRaises(ValueError):
        calc.divide(5, 0)  # sifira bolme sehvi



