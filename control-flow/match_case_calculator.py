"""
Simple Calculator using match-case
----------------------------------
Prompts user for two numbers and an operation,
then performs the calculation and displays the result.
"""

# Step 1: Prompt for user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

# Step 2: Perform the calculation using match-case
match operation:
    case "+":  # Addition
        result = num1 + num2

    case "-":  # Subtraction
        result = num1 - num2

    case "*":  # Multiplication
        result = num1 * num2

    case "/":  # Division
        if num2 == 0:
            result = "Error: Division by zero is not allowed."
        else:
            result = num1 / num2

    case _:  # Default case (invalid operation)
        result = "Error: Invalid operation selected."

# Step 3: Output the result
print("The result is:", result)