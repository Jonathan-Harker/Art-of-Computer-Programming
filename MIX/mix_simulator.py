from typing import List

from MIX.assembler import Assembler
from MIX.functions.store_a import store_a
from fundamentals.mix_instruction import MixInstruction
from fundamentals.mix_word import MixWord

NULL_WORD = MixWord(sign="+", bytes=(0, 0, 0, 0, 0))


class MixSimulator:
    def __init__(self):
        self.ra: MixWord = NULL_WORD
        self.memory: List[MixWord] = [NULL_WORD] * 4000
        self.user_input = []
        self.markers = {}
        self.pc = 0

    def run(self):
        assembler = Assembler()
        assembler.user_input = self.user_input
        assembler.memory = self.memory

        assembler.assemble()

        self.markers = assembler.markers
        self.pc = assembler.pc

        while self.pc < 4000:
            word = self.memory[self.pc]
            instruction = word.as_instruction()
            self.pc += 1
            self._run_instruction(instruction=instruction, word=word)

    def _run_instruction(self, instruction, word: MixWord):
        dispatch_table = {
            0: self.null,
            4: self.div,
            5: self.special,
            7: self.move,
            8: self.load_a,
            24: store_a,
            39: self.jump,
        }

        dispatch_table[instruction.opcode](instruction=instruction, memory=self.memory, ra=self.ra)

    def null(self, instruction: MixInstruction, memory: List[MixWord], ra: MixWord):
        pass

    def div(self, instruction: MixInstruction, memory: List[MixWord], ra: MixWord):
        pass

    def load_a(self, instruction: MixInstruction, memory: List[MixWord], ra: MixWord):
        source = self.memory[instruction.address]
        self.ra = source.field_value(instruction.field)

    def jump(self, instruction: MixInstruction, memory: List[MixWord], ra: MixWord):
        self.pc = instruction.address

    def move(self, instruction: MixInstruction, memory: List[MixWord], ra: MixWord):
        pass

    def special(self, instruction: MixInstruction, memory: List[MixWord], ra: MixWord):
        # add field 0 and 1 for NUM and CHAR ops
        if instruction.field == 2:
            self.pc = 4000
