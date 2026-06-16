from bit import Bit

REG_BITS = 8
REG_MAX = (1 << REG_BITS) - 1


class Register:
    def __init__(self):
        self.bits = [Bit() for _ in range(8)]

    def read(self):
        for _ in range(REG_BITS):
            bits = [bit.read() for bit in self.bits]
        return bits

    def load(self, byte_val: int):
        byte_val = byte_val & REG_MAX
        for bit_idx in range(REG_BITS):
            mask = 1 << bit_idx
            self.bits[bit_idx].set() if (byte_val & mask) else self.bits[
                bit_idx
            ].reset()
