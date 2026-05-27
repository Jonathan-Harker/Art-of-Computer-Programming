import unittest
import uuid

from applications.dataclasses.polynomial import Polynomial
from applications.polynomial_addition import PolynomialAddition


class TestPolynomialAddition(unittest.TestCase):
    def test_simple_addition_is_correct(self):
        pointer_1 = str(uuid.uuid4())
        pointer_2 = str(uuid.uuid4())
        pointer_3 = str(uuid.uuid4())
        pointer_4 = str(uuid.uuid4())

        poly_1 = [
            Polynomial(sign="+", coefficient=1, x_exponent=1, pointer=pointer_1, next=pointer_2),
            Polynomial(sign="+", coefficient=1, y_exponent=1, pointer=pointer_2, next=pointer_3),
            Polynomial(sign="+", coefficient=1, z_exponent=1, pointer=pointer_3, next=pointer_4),
            Polynomial(sign="-", coefficient=0, z_exponent=1, pointer=pointer_4, next=pointer_1),
        ]

        pointer_1 = str(uuid.uuid4())
        pointer_2 = str(uuid.uuid4())
        pointer_3 = str(uuid.uuid4())
        pointer_4 = str(uuid.uuid4())

        poly_2 = [
            Polynomial(sign="+", coefficient=1, x_exponent=2, pointer=pointer_1, next=pointer_2),
            Polynomial(sign="+", coefficient=-2, y_exponent=1, pointer=pointer_2, next=pointer_3),
            Polynomial(sign="+", coefficient=-1, z_exponent=1, pointer=pointer_3, next=pointer_4),
            Polynomial(sign="-", coefficient=0, z_exponent=1, pointer=pointer_4, next=pointer_1),
        ]

        pd = PolynomialAddition(poly_1, poly_2)
        res = pd.add()

        print()
        for item in res:
            print(item)

        self.assertEqual(res[0].__str__(), "x2")
        self.assertEqual(res[1].__str__(), "-y")
        self.assertEqual(res[2].__str__(), "")
        self.assertEqual(res[3].__str__(), "")

        self.assertEqual(res[0].sign, "+")
        self.assertEqual(res[0].x_exponent, 2)
        self.assertEqual(res[1].coefficient, -1)
        self.assertEqual(res[1].y_exponent, 1)
