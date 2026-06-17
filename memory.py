from register import Register

MAX_MEMORY = 4096


class Memory:
    def __init__(self) -> None:
        self.cells = [Register() for _ in range(MAX_MEMORY)]
        # reuse class Register,They have same fundamation

    def read(self, address):
        if 0 <= address < MAX_MEMORY:
            return self.cells[address].read()

    def load(self, address, byte_val: list[int]):
        if 0 <= address < MAX_MEMORY:
            self.cells[address].load(byte_val)
            return self.cells[address].read()
