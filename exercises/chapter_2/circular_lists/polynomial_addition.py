import uuid
from typing import List, Dict

from exercises.chapter_2.circular_lists.polynomial import Polynomial


class PolynomialAddition:
    def __init__(self, poly_p: List[Polynomial], poly_q: List[Polynomial]):
        self.poly_p = poly_p
        self.poly_q = poly_q
        self.map: Dict[str, Polynomial] = {}

    def add(self) -> List[Polynomial]:
        self._setup()

        return self._a1()

    def _a1(self):
        p = self.poly_p[0].pointer
        q_1 = self.poly_q
        q = self.poly_q[0].pointer

        return self.compare(p=p, q=q, q1=q_1)

    # A2
    def compare(self, p: str, q: str, q1: str) -> List[Polynomial]:
        abc_p = self._get_abc(p)
        abc_q = self._get_abc(q)

        if abc_p < abc_q:
            q1 = q
            q = self.map[q].next
            return self.compare(p=p, q=q, q1=q1)

        if abc_p == abc_q:
            # A3
            if abc_p < 0:
                return self.poly_q

            return self._add_coefficients(p, q, q1)

        if abc_p > abc_q:
            return self._a5(p, q, q1)

    def _a5(self, p, q, q1):
        p_poly = self.map[p]
        q2 = str(uuid.uuid4())
        q2_poly = Polynomial(
            sign="+",
            coefficient=p_poly.coefficient,
            pointer=q2,
            next=q,
            x_exponent=p_poly.x_exponent,
            y_exponent=p_poly.y_exponent,
            z_exponent=p_poly.z_exponent,
        )
        self.map[q2] = q2_poly
        q1_poly = self.map[q1]
        q1_poly.next = q2
        q1 = q2
        p = p_poly.next

        return self.compare(p, q, q1)

    def _add_coefficients(self, p: str, q: str, q1: str) -> List[Polynomial]:
        abc_p = self._get_abc(p)

        if abc_p < 0:
            return self.poly_q

        q_poly = self.map[q]
        p_poly = self.map[p]
        q_poly.coefficient += p_poly.coefficient

        if q_poly.coefficient == 0:
            return self._a4(p, q, q1)

        p = p_poly.next
        q_1 = q
        q = q_poly.next

        return self.compare(p=p, q=q, q1=q_1)


    def _a4(self, p: str, q: str, q1: str) -> List[Polynomial]:
        q2 = q
        q1_poly = self.map[q1]
        q1_poly.next = q

        q_poly = self.map[q]
        q = q_poly.next

        p_poly = self.map[p]
        p = p_poly.next

        self.map.pop(q2)

        return self.compare(p, q, q1)

    def _get_abc(self, pointer: str) -> int:
        sign = self.map[pointer].sign
        qx = self.map[pointer].x_exponent
        qy = self.map[pointer].y_exponent
        qz = self.map[pointer].z_exponent
        abc = int(f"{sign}{qx}{qy}{qz}")

        return abc



    def _setup(self):
        for poly in self.poly_p:
            self.map[poly.pointer] = poly

        for poly in self.poly_q:
            self.map[poly.pointer] = poly
