from nbit_ripple_adder import NBitRippleAdder


def alu_op(sub_mode: int):
    def decorator(_func):
        def wrapper(self, a, b):
            b_inv = [x ^ sub_mode for x in b]
            return self.nbra.add(a, b_inv, init_cin=sub_mode)

        return wrapper

    return decorator


class ALU:
    def __init__(self, bit_width) -> None:
        self.bit_width = 8
        self.nbra = NBitRippleAdder(bit_width)

    @alu_op(sub_mode=0)
    def ADD(self, a_bit: list[int], b_bit: list[int]):
        pass

    def SUB(self, a_bit: list[int], b_bit: list[int]):
        pass
