# Simple Calculator Program with Continue Option

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    while True:
        print("\nSimple Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Enter choice (1/2/3/4): ")

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! Please try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        cont = input("Do you want to perform another calculation? (yes/no): ").lower()
        if cont != 'yes':
            print("Thank you for using the calculator!")
            break

# Run the calculator
calculator()
