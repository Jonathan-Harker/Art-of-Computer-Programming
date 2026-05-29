import unittest

from MIX.assembler import Assembler
from fundamentals.mix_word import MixWord
from MIX.mix_simulator import MixSimulator


class TestMixSimulator(unittest.TestCase):
    def test_operation_returns_store_from_stz(self):
        assembler = Assembler()
        op = assembler._operation_to_opcode("STZ")
        self.assertEqual(op, 33)

    def test_parse_to_instruction_returns_correct_instruction_object(self):
        assembler = Assembler()
        word = assembler._convert_instruction(line=" LDA 2000,2(0:3)")
        instruction = word.as_instruction()
        self.assertEqual(word.sign, "+")
        self.assertEqual(instruction.opcode, 8)
        self.assertEqual(instruction.field, 3)
        self.assertEqual(instruction.address, 2000)
        self.assertEqual(instruction.index, 2)

    def test_lda_stores_correct_values_in_register_a(self):
        mix = MixSimulator()
        # memory[2000] = - 1 16 3 5 4 (sign=-,  bytes 1:16, 2:3, 3:5, 4:4)
        mix.memory[2000] = MixWord(sign="-", bytes=(1, 16, 3, 5, 4))

        mix.user_input = [" LDA 2000"]
        mix.run()
        # LDA 2000 with default field (0:5) loads the full word
        self.assertEqual(mix.ra.sign, "-")
        self.assertEqual(mix.ra.bytes, (1, 16, 3, 5, 4))

    def test_custom_function_is_stored(self):
        mix = MixSimulator()
        mix.user_input = ["here LDA 2000"]
        mix.run()
        self.assertEqual(mix.markers["here"], 0)

    def test_custom_function_called_when_referenced(self):
        mix = MixSimulator()
        mix.user_input = [" JMP here", "here LDA 2000"]
        mix.run()
        instruction = mix.memory[0].as_instruction()
        self.assertEqual(instruction.address, 1)

    def test_store_a_overwrites_operation_only(self):
        mix = MixSimulator()
        # rA = + 0 0 0 0 7
        mix.ra = MixWord(sign="+", bytes=(0, 0, 0, 0, 7))
        # memory[2000] = - 1 2 3 4 5
        mix.memory[2000] = MixWord(sign="-", bytes=(1, 2, 3, 4, 5))
        # STA 2000(5:5) stores only byte 5 of rA into byte 5 of memory
        mix.user_input = [" STA 2000(5:5)"]
        mix.run()
        self.assertEqual(mix.memory[2000].sign, "-")
        self.assertEqual(mix.memory[2000].bytes, (1, 2, 3, 4, 7))

    def test_user_input_adds_instructions_to_correct_place(self):
        mix = MixSimulator()
        mix.user_input = [" LDA 0", " ORIG 100", " CON 12345", " ORIG 3000", " LDA 100", " END 3000"]
        mix.run()
        mem = mix.memory[3000].as_instruction()
        ra = mix.ra.bytes

        self.assertEqual(mem.address, 100)
        self.assertEqual(mem.field, 5)
        self.assertEqual(mem.index, 0)
        self.assertEqual(mem.opcode, 8)

        # (3 * 64^2) + 57 = 12345
        self.assertEqual(ra, (0, 0, 3, 0, 57))
