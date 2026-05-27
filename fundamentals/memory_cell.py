from dataclasses import dataclass


@dataclass
class MemoryCell:
    sign: bin
    byte_one_address: bin
    byte_two_address: bin
    byte_three_index_specification: bin
    byte_four_field: bin
    byte_five_operation_code: bin

    def __post_init__(self):
        if len(self._convert_to_text(self.sign)) > 1:
            raise ValueError

        self._assert_binary(self.sign)

        for value in (
                self.byte_one_address,
                self.byte_two_address,
                self.byte_three_index_specification,
                self.byte_four_field,
                self.byte_five_operation_code,
        ):
            if len(self._convert_to_text(value)) > 6:
                raise ValueError

            self._assert_binary(value)

    def _convert_to_text(self, value: bin):
        return str(value).lstrip("0b")

    def _assert_binary(self, value: bin):
        binary_only = str(value).lstrip("0b")
        for char in binary_only:
            if char not in ["0", "1"]:
                raise ValueError


cell_1 = MemoryCell(
    sign=bin(1),
    byte_one_address=bin(63),
    byte_two_address=bin(2),
    byte_three_index_specification=bin(0),
    byte_four_field=bin(0),
    byte_five_operation_code=bin(0),
)
