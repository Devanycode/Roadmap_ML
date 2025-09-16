from art import logo

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 == 0:
        print("It is not possible to divide by 0")
        return None
    else:
        return n1 / n2

def operation_choice():
    list_operations = ['+', '-', '*', '/']
    for symbol in list_operations:
        print(symbol)
    choice_operation = input("Pick an Operation: ")
    while choice_operation not in list_operations:
        print("Enter a valid operation, try again. ")
        choice_operation = input("Pick an Operation: ")
    return choice_operation


def results(operation_result, num1, num2):
    if operation_result == '+':
        return add(num1, num2)
    elif operation_result == '-':
        return sub(num1, num2)
    elif operation_result == '*':
        return mult(num1, num2)
    else:
        return div(num1, num2)

def calculator(num1, num2, operation_selector):
    return results(operation_selector, num1, num2)

calculator_on = True
continue_or_stop = 'n'
result = 0
while calculator_on:
    if continue_or_stop == 'n':
        print(logo)
        number1 = float(input("What is the first number?: "))
        operation = operation_choice()
        number2 = float(input("What is the next number?: "))
        result = calculator(number1, number2, operation)
        print(f"{number1} {operation} {number2} = {result}")
        continue_or_stop = input(f"type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: " )
        if continue_or_stop == 'n':
            print("\n"*20)
    elif continue_or_stop == 'y':
        operation = operation_choice()
        number_now = float(input("What is the next number?: "))
        last_result = calculator(result, number_now, operation)
        print(f"{result} {operation} {number_now} = {last_result}")
        continue_or_stop = input(f"type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: " )
