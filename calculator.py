def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"The result of {num1} + {num2} is {add(num1, num2)}")
            elif choice == '2':
                print(f"The result of {num1} - {num2} is {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result of {num1} * {num2} is {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result of {num1} / {num2} is {divide(num1, num2)}")

        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        
        else:
            print("Invalid input! Please select a valid operation.")

# Run the calculator
calculator()