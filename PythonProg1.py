num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    result = num1 + num2
    print("Result =", result)

elif choice == 2:
    result = num1 - num2
    print("Result =", result)

elif choice == 3:
    result = num1 * num2
    print("Result =", result)

elif choice == 4:
    if num2 != 0:
        result = num1 / num2
        print("Result =", result)
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid choice. Please select a number between 1 and 4.")