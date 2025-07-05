print("Welcome to the Calculator Program")
print("This program allows you to perform basic arithmetic operations: sum, subtract, multiply, and divide.\n")
print("Please select an operation:")
print("""1. Sum
2. Subtract
3. Multiply
4. Divide""")

choice = input("Enter your choice (1-4): ")

x = float(input("Enter the first number: "))

y = float(input("Enter the second number: "))

if operation == "1":
    result = x + y
    print("The result of sum is: " + str(result))
elif operation == "2":
    result = x - y
    print("The result of subtraction is: " + str(result))
elif operation == "3":
    result = x * y
    print("The result of multiplication is: " + str(result))
elif operation == "4":
    if y == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = x / y
        print("The result of division is: " + str(result))
else:
    print("Invalid choice. Please select a valid operation (1-4).")
