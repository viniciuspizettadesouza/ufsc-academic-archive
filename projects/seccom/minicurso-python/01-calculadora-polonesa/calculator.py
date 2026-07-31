
# Calculadora notação polonesa inversa
# para rodar no terminal
#   python -m calculator


def add(a, b):
    return a + b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    return a/b


OPERATIONS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
}


def calculate(user_input):
    tokens = user_input.split()
    operands = []
    operators = []

    for token in tokens:
        if token.isdigit():
            operands.append(int(token))
        else:
            if token in OPERATIONS:
                a = operands.pop()
                b = operands.pop()
                operands.append(OPERATIONS[token](a, b))
            else:
                operators.append(token)

    return operands, operators


if __name__ == '__main__':
    while True:
        user_input = input('Input - ')
        print(calculate(user_input))
