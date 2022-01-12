
#Calculator
from art import logo

#Add
def add(n1, n2):
    return n1 + n2

#Substract
def sub(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {"+": add,
              "-": sub,
              "*": multiply,
              "/": divide
              }

def calculator():
    print(logo)
    n1 = float(input("What's the first number? "))
    proceed = True

    while proceed:
        for i in operations:
            print(i)

        operation_symbol = input("Pick an operation from above: ")
        n2 = float(input("What's the next number? "))
        answer = operations[operation_symbol](n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {round(answer)}")
        
        ask = input("DO you want to make another calculation? Y/N or S to start calc again: ").lower()
        if ask == "y":
            n1 = answer
        elif ask == "s":
            calculator()
        else:
            proceed = False
    

        
calculator()