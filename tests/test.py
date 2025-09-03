import unittest
from src.main import myfunctjpp


class TestMaSeuleFunctionKek(unittest.TestCase):
    def test_classic(self):
        a = 5
        b = 12
        result = a % b
        self.assertEqual(myfunctjpp(a, b), result)

    def test_a_neg(self):
        a = -5
        b = 12
        result = -1
        self.assertEqual(myfunctjpp(a, b), result)
