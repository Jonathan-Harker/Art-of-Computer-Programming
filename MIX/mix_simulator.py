from typing import List

from MIX.instruction_model import Instruction


class MixSimulator:
    def __init__(self):
        null_instruction = Instruction(
            sign="+",
            address=0,
            register=0,
            modification=0,
            operation=0,
        )
        self.ra: Instruction = null_instruction
        self.memory: List[Instruction] = [null_instruction] * 4000
        self.user_input = []
        self.markers = {}

    def run(self):
        for idx, user_instruction in enumerate(self.user_input):
            self.store_markers(line=user_instruction, idx=idx)
            idx += 1

        for idx, user_instruction in enumerate(self.user_input):
            instruction = self.convert_instruction(line=user_instruction)
            self.memory[idx] = instruction
            idx += 1

        for instruction in self.memory:
            self.run_instruction(instruction=instruction)

    def store_markers(self, line: str, idx: int):
        while "  " in line:
            line = line.replace("  ", " ")

        instruction_parts = line.split(" ")
        marker = instruction_parts.pop(0)
        if marker:
            self.markers[marker] = idx

    def convert_instruction(self, line: str) -> Instruction:
        while "  " in line:
            line = line.replace("  ", " ")

        sign = "+"
        register = 0

        instruction_parts = line.split(" ")
        instruction_parts.pop(0)

        modification, register = self.get_modification_value(instruction_parts, register)

        instruction_parts[1] = instruction_parts[1].split("(")[0]
        if instruction_parts[1].isnumeric():
            address = int(instruction_parts[1])
        else:
            address = self.markers[instruction_parts[1]]

        operation = instruction_parts[0]

        return Instruction(
            sign=sign,
            address=address,
            register=register,
            modification=modification,
            operation=self.operation_to_function_no(operation=operation)
        )

    def get_modification_value(self, instruction_parts, register):
        combined_index = "00"
        table = {
            "00": 0,
            "01": 1,
            "02": 2,
            "03": 3,
            "04": 4,
            "05": 5,
            "11": 9,
            "12": 10,
            "13": 11,
            "14": 12,
            "15": 13,
            "22": 18,
            "23": 19,
            "24": 20,
            "25": 21,
            "33": 27,
            "34": 28,
            "35": 29,
            "44": 37,
            "45": 38,
            "55": 39
        }

        second_instruction_part = instruction_parts[1]
        if "," in second_instruction_part:
            address_with_op = instruction_parts[1].split(",")
            instruction_parts[1] = address_with_op[0]
            register = int(address_with_op[1].split("(")[0])
            index_start = address_with_op[1].split("(")[1]
            index_end = address_with_op[2].split(")")[0]

            combined_index = index_start + index_end
        else:
            address_with_op = instruction_parts[1]
            temp = address_with_op.split("(")
            if len(temp) > 1:
                indexes = temp[1].split(":")
                combined_index = indexes[0] + indexes[1].split(")")[0]

        modification = table[combined_index]
        return modification, register


    def operation_to_function_no(self, operation: str) -> int:
        table = {
            "LDA": 8,
            "STZ": 33,
            "JMP": 39,
            "STA": 24,
        }

        return table[operation]

    def run_instruction(self, instruction: Instruction):
        table = {
            0: self.null,
            4: self.div,
            8: self.load_a,
            24: self.store_a,
            39: self.jump,
        }

        table[instruction.operation](instruction=instruction)

    def null(self, instruction: Instruction):
        pass

    def div(self, instruction: Instruction):
        pass

    def load_a(self, instruction: Instruction):
        self.ra = instruction

    def store_a(self, instruction: Instruction):
        table = {
            0: ["s", "a", "r", "m", "o"],
            39: ["o"]
        }

        items_to_modfy = table[instruction.modification]
        if "s" in items_to_modfy:
            self.memory[instruction.address].sign = self.ra.sign
        if "a" in items_to_modfy:
            self.memory[instruction.address].address = self.ra.address
        if "o" in items_to_modfy:
            self.memory[instruction.address].operation = self.ra.operation
        if "r" in items_to_modfy:
            self.memory[instruction.address].register = self.ra.register
        if "m" in items_to_modfy:
            self.memory[instruction.address].modification = self.ra.modification

    def jump(self, instruction: Instruction):
        pass
