from concurrent.futures import ThreadPoolExecutor
from threading import Barrier, Thread

from bit import Bit


class Register:
    def __init__(self, bit_width=8):
        self.bit_width = bit_width
        self.bits = [Bit() for _ in range(self.bit_width)]
        self.clk_barrier = Barrier(bit_width)

    def _sync_write_cell(self, idx: int, val: int):
        self.clk_barrier.wait()
        self.bits[idx].set() if val else self.bits[idx].reset()

    def read(self):
        return [bit.read() for bit in self.bits]

    def load(self, bit_list: list[int]) -> None:
        num = 0
        for idx, bit in enumerate(bit_list):
            num |= bit << idx

        mask = (1 << self.bit_width) - 1
        num &= mask

        full = [(num >> i) & 1 for i in range(self.bit_width)]
        with ThreadPoolExecutor(max_workers=self.bit_width) as pool:
            tasks = [
                pool.submit(self._sync_write_cell, idx, val)
                for idx, val in enumerate(full)
            ]
            for task in tasks:
                task.result()
