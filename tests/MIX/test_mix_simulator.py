import unittest

from MIX.instruction_model import Instruction
from MIX.mix_simulator import MixSimulator


class TestMixSimulator(unittest.TestCase):
    def test_operation_returns_store_from_stz(self):
        mix = MixSimulator()
        op = mix.operation_to_function_no(operation="STZ")
        self.assertEqual(op, 33)

    def test_parse_to_instruction_returns_correct_instruction_object(self):
        mix = MixSimulator()
        instruction = mix.convert_instruction(line=" LDA 2000,2(0,3)")
        self.assertEqual(instruction.sign, "+")
        self.assertEqual(instruction.operation, 8)
        self.assertEqual(instruction.modification, 3)
        self.assertEqual(instruction.address, 2000)
        self.assertEqual(instruction.register, 2)

    def test_lda_stores_correct_values_in_register_a(self):
        mix = MixSimulator()
        mix.memory[2000] = Instruction(
            sign="-",
            address=80,
            register=3,
            modification=5,
            operation=4
        )

        mix.user_input = [" LDA 2000"]
        mix.run()
        self.assertEqual(mix.ra.sign, "+")
        self.assertEqual(mix.ra.address, 2000)
        self.assertEqual(mix.ra.operation, 8)

    def test_custom_function_is_stored(self):
        mix = MixSimulator()
        mix.user_input = ["here LDA 2000"]
        mix.run()
        self.assertEqual(mix.markers["here"], 0)

    def test_custom_function_called_when_referenced(self):
        mix = MixSimulator()
        mix.user_input = [" JMP here", "here LDA 2000"]
        mix.run()
        self.assertEqual(mix.memory[0].address, 1)
