# This script calculates projected savings after one year

monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your monthly expenses:"))
monthly_savings = monthly_income - monthly_expenses

print(f"Your monthly savings is: ${monthly_savings}")

annual_savings = monthly_savings * 12
interest_rate = 0.05
annual_interest_rate = 0.05 * 12

projected_savings = annual_savings + (annual_savings * annual_interest_rate)

print(f"Projected savings after one year, with interest, is: ${projected_savings}")