from dataclasses import dataclass


@dataclass
class Instruction:
    sign: str
    address: int
    register: int
    modification: int
    operation: int
