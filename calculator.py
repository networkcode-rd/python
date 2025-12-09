def add(n1, n2):
    return n1 + n2

def subtract (n1,n2):
    return n1 - n2

def multiply(n1,n2):
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
    wants_to_continue = True
    first_number = float(input("Type the first number: "))

    while wants_to_continue:

        for symbol in operations:
            print(symbol)
        operator_symbol = input("Pick an operation: ")
        second_number = float(input("Type the second number: "))
        answer = operations[operator_symbol](first_number, second_number)
        print(f"{first_number} {operator_symbol} {second_number} = {answer}")

        choice = input(f"Type 'y' to continue calculating with existing answer {answer}. or type 'n' to start a new calculation: ")

        if choice == "y":
            first_number = answer
        else:
            wants_to_continue = False
            print("\n" * 20)
            calculator()

calculator()
