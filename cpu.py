class Cpu:
    def __init__(self):
        self.reg = {"A": 0, "B": 0, "C": 0, "D": 0}

        self.pc = 0
        self.z = 0
        self.memory = [0] * 4096
        self.running = True

    def readline(self, program):
        if self.pc < len(program):
            instruction = program[self.pc]

            self.pc += 1
            return instruction

        self.running = False
        return None

    def splitInstruction(self, instruction):
        parts = instruction.split()
        return parts
