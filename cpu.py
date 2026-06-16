from register import Register


class Cpu:
    # hardware infomation
    REG_BITS = 8
    REG_MAX = (1 << REG_BITS) - 1

    def __init__(self):
        self.reg = [Register(), Register(), Register(), Register()]
        self.pc = 0
        self.z = 0
        self.memory = [0] * 4096
        self.state = "HALTED"  # RUNNING/HALTED/ERROR/RESET

    def _set_reg(self, address, value):
        value = value & self.REG_MAX
        self.reg[address] = value
        self.z = 1 if value == 0 else 0

    def get_bin_str(self, address):
        val = self.reg[address]
        return format(val, f"0{self.REG_BITS}b")

    def readline(self, program):

        if self.state != "RUNNING":
            return None

        if self.pc < len(program):
            instruction = program[self.pc]

            self.pc += 1
            return instruction

        self.running = False
        return None

    def splitInstruction(self, instruction):
        parts = instruction.strip().split()
        return parts
