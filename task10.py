import unittest

class Calculator:
    """Sadə kalkulyator sinfi riyazi əməliyyatlar üçün."""

    def add(self, a, b):
        """İki ədədi toplayır."""
        return a + b

    def subtract(self, a, b):
        """İki ədədi çıxır."""
        return a - b

    def multiply(self, a, b):
        """İki ədədi vurur."""
        return a * b

    def divide(self, a, b):
        """İki ədədi bölür. Sıfıra bölmə zamanı ValueError verir."""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b


class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(-1, 1), 0)

    def test_subtract(self):
        calc = Calculator()
        self.assertEqual(calc.subtract(5, 3), 2)
        self.assertEqual(calc.subtract(3, 5), -2)  # Düzgün cavab -2-dir

    def test_multiply(self):
        calc = Calculator()
        self.assertEqual(calc.multiply(4, 3), 12)  # "mutiply" yox, "multiply" olmalıdır
        self.assertEqual(calc.multiply(-1, 3), -3)

    def test_divide(self):
        calc = Calculator()
        self.assertEqual(calc.divide(10, 2), 5)
        self.assertEqual(calc.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            calc.divide(5, 0)  # Sıfıra bölmə səhvi test edilir


if __name__ == "__main__":
    unittest.main()
