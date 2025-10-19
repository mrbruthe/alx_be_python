def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return "Error: Non-numeric input."

    try:
        result = num / denom
        # Return result in exact sentence format
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Division by zero."
