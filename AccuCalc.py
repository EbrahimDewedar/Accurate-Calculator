def add(n1, n2):
    return n1 +n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {"+" : add , "-" : subtract , "*" : multiply , "/" : divide}

def calculator():
    num1 = float(input("what is the first number:"))
    should_accumulate = True
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        symbol_operation = input("pick an operation")
        num2 = float(input("what is the nexy number:"))
        answer = operations[symbol_operation](num1, num2)
        print(f"{num1} {symbol_operation} {num2} = {answer}")
        choice = input(f"type 'y' if you want to continue with {answer} or 'n' to another number ")
        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" *20)
            calculator()

calculator()