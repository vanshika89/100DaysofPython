def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    should_accumulate = True
    number1 = float(input("What's the first number?: "))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation: ")
        if operation in operations:
            number2 = float(input("What's the next number?: "))
            answer = operations[operation](number1, number2)
            print(f"{number1} {operation}{number2} = {answer}")
        else:
            print("Choose from given operations: ")

        choice = input(f"Do you want to continue with calculating with {answer}? tyoe 'y' for yes and 'n' for no:")
        if choice == 'y':
            number1 = answer
        else:
            should_accumulate = False
            print('\n' * 20)
            calculator()


calculator()
