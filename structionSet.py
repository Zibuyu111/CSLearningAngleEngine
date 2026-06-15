from cpu import Cpu


class StructionSet:
    def __init__(self, cpu_instance: Cpu) -> None:
        self.cpu = cpu_instance

    def RUN(self):
        self.cpu.state = "RUNNING"
        return self.cpu.state

    def HALT(self) -> None:
        self.cpu.state = "HALTED"

    def RESET(self):
        self.cpu.reg = {"A": 0, "B": 0, "C": 0, "D": 0}
        self.cpu.pc = 0
        self.cpu.z = 0
        self.cpu.memory = [0] * 4096
        self.cpu.state = "HALTED"  # RUNNING/HALTED/ERROR/RESET
        return self.cpu.state

    def MOV(self, address, info):
        self.cpu.reg[address] = info
        return self.cpu.reg

    def ADD(self, addressA, addressB):
        return self.cpu.reg[addressA] + self.cpu.reg[addressB]
