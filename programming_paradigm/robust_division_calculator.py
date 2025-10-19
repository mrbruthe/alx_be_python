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
        return "Error: Non-numeric input."

    try:
        result = num / denom
        return result
    except ZeroDivisionError:
        return "Error: Division by zero."
