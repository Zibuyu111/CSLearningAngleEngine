from register import Register

MAX_MEMORY = 4096


class Memory:
    def __init__(self) -> None:
        self.cells = [Register() for _ in range(MAX_MEMORY)]
        # reuse class Register,They have same fundamation

    def read(self, address):
        bit_ls = "".join(map(str, address))
        bit_int = int(bit_ls, 2)
        if 0 <= bit_int < MAX_MEMORY:
            return self.cells[bit_int].read()

    def load(self, address: list[int], byte_val: list[int]):
        try:
            bit_ls = "".join(map(str, address))
            bit_int = int(bit_ls, 2)
            if 0 <= bit_int < MAX_MEMORY:
                self.cells[int(bit_ls, 2)].load(byte_val)
                return self.cells[bit_int].read()
        except (ValueError, TypeError):
            return 0
