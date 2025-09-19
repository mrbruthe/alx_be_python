# Step 1: Prompt the user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Step 2: Generate the multiplication table using a for loop
for i in range(1, 11):
    z = number * i
    print(f"{number} * {i} = {z}")