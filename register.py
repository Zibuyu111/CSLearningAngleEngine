import re

from bit import Bit


class Register:
    def __init__(self, bit_width=8):
        self.bit_width = bit_width
        self.bits = [Bit() for _ in range(self.bit_width)]

    def read(self):
        return [bit.read() for bit in self.bits]

    def load(self, bit_list: list[int]) -> None:
        num = 0
        for idx, bit in enumerate(bit_list):
            if bit:
                num |= 1 << idx

        mask = (1 << self.bit_width) - 1
        num = num & mask

        full = []
        temp = num
        for _ in range(self.bit_width):
            full.append(temp & 1)
            temp >>= 1
        for bit_idx in range(self.bit_width):
            self.bits[bit_idx].set() if full[bit_idx] else self.bits[bit_idx].reset()
