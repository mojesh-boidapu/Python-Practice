#arithmatic calculator
#Method 2
import os
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
operation_dict={
    '+':add,
    '-':sub,
    '*':mul,
    '/':div,
}
def calculator():
    print("Available operations: +  -  *  /")
    number1=float(input("Enter the first number: "))
    for symbol in operation_dict:
        print(symbol)
    end = True
    while end:
        op_symbol=input("Enter the operation: ")
        number2=float(input("Enter the second number: "))
        calculator_function=operation_dict[op_symbol]
        output=calculator_function(number1,number2)
        print(f"{number1}{op_symbol}{number2}={output}")
        do_again=input(f"Enter 'y' to continue calculation or 'n' for new calculation or 'x' to exit:\n")
        if do_again=='y':
            number1=output
        elif do_again=='n':
            end=False
            os.system('cls')
            calculator()
        else:
            end=False
calculator()