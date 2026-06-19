from register import Register

IR_MAXBIT = 8


class InstructionRegister(Register):
    def __init__(self):
        super().__init__(IR_MAXBIT)
