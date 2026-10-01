## main.py
import operator
from typing import List

def do_algebra(operators: List[str], operands: List[int]) -> int:
    """ 
    Given two lists operator and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebraic 
    expression and return the evaluation of this expression.

    Parameters:
    - operators: A list of strings representing algebraic operations ('+', '-', '*', '//', '**').
    - operands: A list of integers (non-negative) to be used in the expression.

    Returns:
    - An integer result of the evaluated expression.

    Raises:
    - ValueError: If the input lists are invalid.
    """
    # Validate input lists
    if not isinstance(operators, list) or not isinstance(operands, list):
        raise ValueError("Both operators and operands must be lists.")
    
    if len(operators) + 1 != len(operands):
        raise ValueError("The number of operands must be one more than the number of operators.")
    
    valid_operators = {'+', '-', '*', '//', '**'}
    for op in operators:
        if op not in valid_operators:
            raise ValueError(f"Invalid operator: {op}")

    for num in operands:
        if not isinstance(num, int) or num < 0:
            raise ValueError("All operands must be non-negative integers.")

    # Construct and evaluate the expression
    result = operands[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result = operator.add(result, operands[i + 1])
        elif operators[i] == '-':
            result = operator.sub(result, operands[i + 1])
        elif operators[i] == '*':
            result = operator.mul(result, operands[i + 1])
        elif operators[i] == '//':
            if operands[i + 1] == 0:
                raise ValueError("Division by zero is not allowed.")
            result = operator.floordiv(result, operands[i + 1])
        elif operators[i] == '**':
            result = operator.pow(result, operands[i + 1])

    return result
