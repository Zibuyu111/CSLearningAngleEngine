import re
from typing import Self

import myprogram
from cpu import Cpu
from memory import Memory
from program_counter import ProgramCounter
from register import Register
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

"""print(myprogram.program)
myCpupu = Cpu()
myInstruction = StructionSet(myCpu)

myInstruction.RUN()
ans = 0
while myCpu.state == "RUNNING":
    instruction = myCpu.readline(myprogram.program)
    if instruction is None:
        break
    command, *args = myCpu.splitInstruction(instruction)

    if command == "MOV":
        myInstruction.MOV(*args)
    if command == "ADD":
        ans = myInstruction.ADD(*args)
    if command == "HALT":
        print(myCpu.state, myCpu.reg, ans)

        myInstruction.HALT()"""
"""
register = Register()

register.load(ord("A"))
print("RUNNING")
print(register.read())
print(chr(int("".join(map(str, reversed(register.read()))), 2)))
"""
"""
pc = ProgramCounter()
print("new program_counter")
print(pc.read())
print("load basic data")
print("pc.jump([1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1])")
pc.jump([1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1])
print("increment")
pc.increment()
print(pc.read())
"""

# MOV = 0001 ADD = 0010 HALT = 0011

memory = Memory()
pc = ProgramCounter()
a = memory.load([0, 0, 0, 0], [0, 0, 0, 1])
b = memory.load([0, 0, 0, 1], [0, 0, 1, 0])
c = memory.load([0, 0, 1, 0], [0, 0, 1, 1])
print(a, b, c)

pc.jump([0, 0, 0, 0])
d = memory.read(pc.read())
pc.increment()
print("increment")
p = memory.read(reversed(pc.read()))
print(d, p)
