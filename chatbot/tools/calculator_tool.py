import operator
import re

# Supported operators
OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

def safe_calculate(expression: str) -> str:
    """
    Evaluates a simple arithmetic expression safely.
    Supports: +, -, *, /
    Example: "5 + 3"
    """
    try:
        # Remove all whitespace
        expression = expression.strip().replace(" ", "")

        # Regex to match simple binary arithmetic expressions
        match = re.match(r'^(-?\d+\.?\d*)([+\-*/])(-?\d+\.?\d*)$', expression)
        if not match:
            return "(Invalid format. Use format like '5 + 2')"

        left, op, right = match.groups()
        left, right = float(left), float(right)

        if op in OPERATORS:
            result = OPERATORS[op](left, right)
            return str(result)
        else:
            return "(Unsupported operation.)"

    except ZeroDivisionError:
        return "(Cannot divide by zero.)"
    except Exception as e:
        return f"(Error in calculation: {str(e)})"