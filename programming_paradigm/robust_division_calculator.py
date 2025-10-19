def safe_divide(numerator, denominator):
    """
    Performs division of numerator by denominator with robust error handling.

    Handles:
    - Division by zero
    - Non-numeric inputs
    """
    try:
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / denom
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
