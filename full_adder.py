from half_adder import HalfAdder
from nbit_ripple_adder import nbit_ripple_adder


class FullAdder:
    def __init__(self) -> None:
        self.ha1, self.ha2 = HalfAdder(), HalfAdder()

    def or_gate(self, setA: int, setB: int):
        return setA | setB

    def full_adder(self, setA: int, setB: int, Carry_in: int) -> tuple[int, int]:
        sum1, carry1 = self.ha1(setA, setB)
        sum, carry2 = self.ha2(sum1, Carry_in)
        carry = self.or_gate(carry1, carry2)
        return sum, carry
