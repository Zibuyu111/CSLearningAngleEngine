from full_adder import FullAdder


class NBitRippleAdder:
    def __init__(self, bit_width: int):
        self.bit_width = bit_width
        self.fa = FullAdder()

    def add(self, a_bits: list[int], b_bits: list[int]):
        cin = 0
        sum_bits = [0] * self.bit_width
        for i in range(self.bit_width):
            s, cout = self.fa.full_adder(a_bits[i], b_bits[i], cin)
            sum_bits[i] = s
            cin = cout
        return sum_bits, cin
