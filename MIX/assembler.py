from typing import List

from fundamentals.mix_word import MixWord

NULL_WORD = MixWord(sign="+", bytes=(0, 0, 0, 0, 0))
OP_TABLE = {
    "LDA": 8,
    "STZ": 33,
    "JMP": 39,
    "STA": 24,
    "MOVE": 7,
    "HLT": 5,
}


class Assembler:
    def __init__(self):
        self.memory: List[MixWord] = [NULL_WORD] * 4000
        self.user_input = []
        self.markers = {}
        self.pc = 0

    def assemble(self):
        self._store_markers()
        self._compile_instructions()

    def _store_markers(self):
        location = 0
        for user_instruction in self.user_input:
            if self._is_directive(line=user_instruction, directive="END"):
                break

            if self._is_directive(line=user_instruction, directive="ORIG"):
                location = self._parse_address(line=user_instruction, directive="ORIG")
                continue

            self._store_marker(line=user_instruction, idx=location)
            location += 1

    def _compile_instructions(self):
        location = 0
        for user_instruction in self.user_input:
            if self._is_directive(line=user_instruction, directive="END"):
                address = self._parse_address(line=user_instruction, directive="END")
                self.pc = address
                break

            if self._is_directive(line=user_instruction, directive="ORIG"):
                location = self._parse_address(line=user_instruction, directive="ORIG")
                continue

            if self._is_directive(line=user_instruction, directive="CON"):
                value = self._parse_address(line=user_instruction, directive="CON")
                self.memory[location] = self._value_to_word(value)
            else:
                instruction = self._convert_instruction(line=user_instruction)
                self.memory[location] = instruction
            location += 1

    def _convert_instruction(self, line: str) -> MixWord:
        line = self._reduce_whitespace(line)

        sign = "+"
        index = 0

        instruction_parts = line.split(" ")
        instruction_parts.pop(0)

        field, index = self._get_field_and_index(instruction_parts, index)

        instruction_parts[1] = instruction_parts[1].split("(")[0]
        if instruction_parts[1].isnumeric():
            address = int(instruction_parts[1])
        else:
            address = self.markers[instruction_parts[1]]

        opcode = self._operation_to_opcode(instruction_parts[0])

        addr_hi = address // 64
        addr_lo = address % 64

        return MixWord(
            sign=sign,
            bytes=(addr_hi, addr_lo, index, field, opcode),
        )

    def _operation_to_opcode(self, operation: str) -> int:
        return OP_TABLE[operation]

    def _is_directive(self, line: str, directive: str) -> bool:
        line = self._reduce_whitespace(line)
        parts = line.strip().split(" ")

        return directive in parts

    def _parse_address(self, line: str, directive: str) -> int:
        line = self._reduce_whitespace(line)
        parts = line.strip().split(" ")
        directive_idx = parts.index(directive)

        return int(parts[directive_idx + 1])

    def _store_marker(self, line: str, idx: int):
        line = self._reduce_whitespace(line)

        instruction_parts = line.split(" ")
        marker = instruction_parts.pop(0)
        if marker:
            self.markers[marker] = idx

    def _value_to_word(self, value: int) -> MixWord:
        sign = "-" if value < 0 else "+"
        remaining = abs(value)
        byte_values = []
        for _ in range(5):
            byte_values.append(remaining % 64)
            remaining //= 64

        byte_values.reverse()

        return MixWord(sign=sign, bytes=tuple(byte_values))

    def _get_field_and_index(self, instruction_parts, index):
        left = 0
        right = 5

        second_instruction_part = instruction_parts[1]
        if "," in second_instruction_part:
            address_with_op = instruction_parts[1].split(",")
            instruction_parts[1] = address_with_op[0]
            remainder = address_with_op[1]
            if "(" in remainder:
                index = int(remainder.split("(")[0])
                field_part = remainder.split("(")[1].rstrip(")")
                left = int(field_part.split(":")[0])
                right = int(field_part.split(":")[1])
            else:
                index = int(remainder)
        else:
            address_with_op = instruction_parts[1]
            temp = address_with_op.split("(")
            if len(temp) > 1:
                indexes = temp[1].split(":")
                left = int(indexes[0])
                right = int(indexes[1].split(")")[0])

        field = left * 8 + right

        return field, index

    def _reduce_whitespace(self, line: str) -> str:
        while "  " in line:
            line = line.replace("  ", " ")

        return line
