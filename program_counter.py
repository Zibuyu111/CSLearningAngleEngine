from nbit_ripple_adder import NBitRippleAdder
from register import Register

MAX_BIT = 12  # memory is 2^12
nbra = NBitRippleAdder(bit_width=MAX_BIT)


class ProgramCounter(Register):
    def __init__(self) -> None:
        super().__init__(bit_width=MAX_BIT)
        self.one = [0] * MAX_BIT
        self.one[0] = 1

    def increment(self):
        next_sequence, _ = nbra.add(self.read(), self.one)
        self.load(next_sequence)

    def jump(self, target):
        self.load(target)
