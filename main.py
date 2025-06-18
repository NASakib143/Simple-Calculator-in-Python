print("Welcome to the Calculator Program")
print("This program allows you to perform basic arithmetic operations: sum, subtract, multiply, and divide.\n")
print("Please select an operation:")
print("""1. Sum
2. Subtract
3. Multiply
4. Divide""")

choice = input("Enter your choice (1-4): ")

A = float(input("Enter the first number: "))

B = float(input("Enter the second number: "))

if choice == "1":
    result = A + B
    print("The result of sum is: " + str(result))
elif choice == "2":
    result = A - B
    print("The result of subtraction is:" + str(result))
elif choice == "3":
    result = A * B
    print("The result of Multiply is: " + str(result))
elif choice == "4":
    if B == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = A / B
        print("The result of Divide is: " + str(result))
else:
    print("Invalid choice. Please select a valid operation (1-4).")
