class HalfAdder:
    def __init__(self) -> None:
        pass

    def and_gate(self, setA: int, setB: int):
        return setA & setB

    def xor_gate(self, setA: int, setB: int):
        return setA ^ setB

    def halfadder(self, setA: int, setB: int) -> tuple[int, int]:
        sum = self.xor_gate(setA, setB)
        carry = self.and_gate(setA, setB)
        return sum, carry
