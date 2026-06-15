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
myCpu = Cpu()
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

        myInstruction.HALT()
