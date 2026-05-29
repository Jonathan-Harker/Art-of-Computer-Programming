from dataclasses import dataclass


@dataclass
class MixInstruction:
    address: int
    index: int
    field: int
    opcode: int
