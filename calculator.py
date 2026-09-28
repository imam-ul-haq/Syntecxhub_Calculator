def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


while True:

    print("\n1. Calculate")
    print("2. Clear")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        try:
            num1 = int(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = int(input("Enter second number: "))

            if operator == "+":
                result = add(num1, num2)

            elif operator == "-":
                result = subtract(num1, num2)

            elif operator == "*":
                result = multiply(num1, num2)

            elif operator == "/":
                result = divide(num1, num2)

            else:
                print("Invalid operator")
                continue

            print("Result =", result)

        except ValueError:
            print("Please enter a valid number")

    elif choice == "2":
        print("Calculator cleared")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")