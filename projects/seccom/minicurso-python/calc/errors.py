class CalculatorError(Exception):
    pass


class NotEnoughValuesError(CalculatorError):
    pass


class UnknownOperatorError(CalculatorError):
    pass


class TooManyValuesOnStackError(CalculatorError):
    pass
