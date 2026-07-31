import math

from .errors import NotEnoughValuesError


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def binary_op(f):
    def inner(stack):
        if len(stack) < 2:
            raise NotEnoughValuesError("Stack does not have enough operands.")

        a = stack.pop()
        b = stack.pop()
        return f(a, b)
    return inner


def unary_op(f):
    def inner(stack):
        try:
            a = stack.pop()
        except IndexError as e:
            raise NotEnoughValuesError(
                "Stack does not have enough operands.") from e

        return f(a)
    return inner


OPERATIONS = {
    '+': binary_op(add),
    '-': binary_op(sub),
    '*': binary_op(mul),
    '/': binary_op(div),
    'sqrt': unary_op(math.sqrt),
}
