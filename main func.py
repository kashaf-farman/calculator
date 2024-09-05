from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide



def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_operator():
    while True:
        op = input("Enter operator (+, -, *, /): ").strip()
        if op in ['+', '-', '*', '/']:
            return op
        else:
            print("Invalid operator. Please enter one of +, -, *, /.")


def perform_calculation(x, y, op):
    if op == '+':
        return add(x, y)
    elif op == '-':
        return subtract(x, y)
    elif op == '*':
        return multiply(x, y)
    elif op == '/':
        return divide(x, y)


def main():
    while True:
        print("Simple Calculator")
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        operator = get_operator()

        result = perform_calculation(num1, num2, operator)
        print(f"The result of {num1} {operator} {num2} is: {result}")

        quit_choice = input("Do you want to quit the calculator? (Y for Yes, N for No): ").strip().upper()
        if quit_choice == 'Y':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()

