from dataclasses import dataclass

from fundamentals.mix_instruction import MixInstruction


@dataclass
class MixWord:
    sign: str
    bytes: tuple[int, int, int, int, int]

    def __post_init__(self):
        if self.sign not in ("+", "-"):
            raise ValueError("Sign must be '+' or '-'")

        if any(not (0 <= b <= 63) for b in self.bytes):
            raise ValueError("Each byte must be in range 0..63")

    def field_value(self, field: int) -> "MixWord":
        left = field // 8
        right = field % 8

        if left == 0:
            sign = self.sign
            left = 1
        else:
            sign = "+"

        selected = self.bytes[left - 1:right]
        padding = (0,) * (5 - len(selected))
        return MixWord(sign=sign, bytes=padding + tuple(selected))

    def as_instruction(self) -> MixInstruction:
        address = self.bytes[0] * 64 + self.bytes[1]
        if self.sign == "-":
            address = -address

        return MixInstruction(
            address=address,
            index=self.bytes[2],
            field=self.bytes[3],
            opcode=self.bytes[4],
        )
