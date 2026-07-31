from .calculator import calculate
from .errors import CalculatorError

while True:
    try:
        user_input = input('>> ')
    except (KeyboardInterrupt, EOFError):
        print()
        break

    try:
        print(calculate(user_input))
    except CalculatorError as e:
        print(e)
