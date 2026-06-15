import myprogram
from cpu import Cpu
from structionSet import StructionSet

"""
print(myprogram.program)
mycpu = Cpu()
while mycpu.running:
    instruction = mycpu.readline(myprogram.program)
    if instruction is None:
        break
    print(f"current pc address:{mycpu.pc},carry out instruction:{instruction}")
"""

print(myprogram.program)
mycpu = Cpu()
while mycpu.running:
    instruction = mycpu.readline(myprogram.program)
    if instruction is None:
        break
    command, register = mycpu.splitInstruction(instruction)
    myStructionSet = StructionSet()
