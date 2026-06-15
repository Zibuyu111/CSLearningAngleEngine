from cpu import Cpu


class StructionSet:
    def __init__(self, cpu_instance: Cpu) -> None:
        self.cpu = cpu_instance
        self.address = ""

    def set_address(self, addr):
        self.address = addr

    def MOV(self, info):
        self.cpu.reg[self.address] = info
        return self.cpu.reg

    def ADD(self, addressA, addressB):
        return self.cpu.reg[addressA] + self.cpu.reg[addressB]
