import unittest

# Funktion, die wir testen wollen:


def add(x, y):
    return x + y

# Klasse zum Testen


class TestAddFunction(unittest.TestCase):
    def test_add2_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)


if __name__ == '__main__':
    unittest.main()
