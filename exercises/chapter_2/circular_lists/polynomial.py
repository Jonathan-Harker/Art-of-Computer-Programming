from dataclasses import dataclass
from typing import Literal


@dataclass
class Polynomial:
    sign: Literal["-", "+"]
    coefficient: int
    pointer: str
    next: str
    x_exponent: int = 0
    y_exponent: int = 0
    z_exponent: int = 0

    def __str__(self):
        out = ""

        if self._is_sentinel():
            return out

        if self.sign == "-":
            out += self.sign

        if self.coefficient != 1:
            if self.coefficient == -1:
                out += "-"
            elif self.coefficient == 0:
                return ""
            else:
                out += str(self.coefficient)

        if self.x_exponent != 0:
            if self.x_exponent == 1:
                out += "x"
            else:
                out += f"x{self.x_exponent}"

        if self.y_exponent != 0:
            if self.y_exponent == 1:
                out += "y"
            else:
                out += f"y{self.y_exponent}"

        if self.z_exponent != 0:
            if self.z_exponent == 1:
                out += "z"
            else:
                out += f"z{self.z_exponent}"

        return out

    def _is_sentinel(self) -> bool:
        return self.sign == "-" and self.coefficient == 0 and self.x_exponent == 0 and self.y_exponent == 0 and self.z_exponent == 1
