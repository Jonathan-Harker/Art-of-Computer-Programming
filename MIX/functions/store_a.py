from fundamentals.mix_instruction import MixInstruction
from fundamentals.mix_word import MixWord


def store_a(instruction: MixInstruction, memory: list[MixWord], ra: MixWord) -> None:
    # the field spec (L:R) is encoded as a single byte value using the formula L * 8 + R.
    left = instruction.field // 8
    right = instruction.field % 8

    dest = memory[instruction.address]
    dest_bytes = list(dest.bytes)

    if left == 0:
        sign = ra.sign
        left = 1
    else:
        sign = dest.sign

    num_bytes = right - left + 1
    ra_bytes = ra.bytes[5 - num_bytes:]

    for i, pos in enumerate(range(left - 1, right)):
        dest_bytes[pos] = ra_bytes[i]

    memory[instruction.address] = MixWord(sign=sign, bytes=tuple(dest_bytes))
