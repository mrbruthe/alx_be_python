# pattern_drawing.py

pattern_size = int(input("Enter the size of the pattern: "))

i = 1
while i <= pattern_size:   # controls rows
    for j in range(pattern_size):  # controls columns
        print("*", end="")  
    print()  # move to next line after each row
    i += 1