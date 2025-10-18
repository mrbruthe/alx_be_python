
def perform_operation(num1, num2, operation):
    """Performs the specified arithmetic operation on two numbers."""
    operations = {
        'add': addition,
        'subtract': subtraction,
        'multiply': multiplication,
        'divide': division
    }
    
    if operation not in operations:
        raise ValueError(f"Invalid operation '{operation}'. Supported operations are: {', '.join(operations.keys())}.")
    
    return operations[operation](num1, num2)

def addition(num1, num2):
  """Returns the sum of two numbers."""
  return num1 + num2

def subtraction(num1, num2):
    """Returns the difference of two numbers."""
    return num1 - num2

def multiplication(num1, num2):
    """Returns the product of the two numbers."""
    return num1 * num2

def division(num1, num2):
    """Returns the quotient of the two numbers. Raises ValueError on division by zero."""
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2
