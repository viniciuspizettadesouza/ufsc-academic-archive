import re

from .operations import OPERATIONS
from .errors import UnknownOperatorError, TooManyValuesOnStackError

FLOAT_RE = re.compile(r'-?(([0-9]+)|([0-9]+\.[0-9]+))')


def calculate(user_input):
    tokens = user_input.split()

    operands = []

    for token in tokens:
        if FLOAT_RE.fullmatch(token):
            operands.append(float(token))
        else:
            if token in OPERATIONS:
                operands.append(OPERATIONS[token](operands))
            else:
                raise UnknownOperatorError(f'Operator "{token}" is not valid.')

    try:
        [result] = operands
    except ValueError:
        raise TooManyValuesOnStackError(
            f'Too many operands still in stack: {operands}.')

    return result
