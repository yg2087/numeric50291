###
## Basic online calculator
###

## Here I have defined four functions for the four
## basic operations. 
##
## 1) You should provide an interface
## function that will prompt the user for input and
## call the appropriate function based on the user's
## input. The interface function should continue to
## prompt the user for input until the user enters
## 'exit'. 
##
## 2) The interface function should also handle
## any exceptions that might be thrown by the basic
## operations functions. If an exception is thrown,
## the interface function should print an error message
## and continue to prompt the user for input.
##
## 3) Add other "operations" to the calculator, that
## involve complicated operations (e.g., trigonometric
## functions, logarithms, etc.).

def Addition(a, b):
    """Add two numbers."""
    return a + b

def Subtraction(a, b):
    """Subtract one number from another."""
    return a - b

def Multiplication(a, b):
    """Multiply two numbers."""
    return a * b
    

def Division(a, b):
    """Divide one number by another."""
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
    


import pandas as pd



def input_ques():
    input_prompts = [0,1,2,3]
    operation_names = ["Addition", "Subtraction", "Multiplication", "Division"]
    operations = [Addition, Subtraction, Multiplication, Division]
    calc_menu = pd.DataFrame({"Input Prompts": input_prompts, "Operations": operation_names}, index = input_prompts)
    print(calc_menu)
    user_input = input(f"To calculate a function, enter the index and the input values in the folowing format: [Input Prompt](input1,input2,...)")
    try:    
        a = int(user_input[2])
        b = int(user_input[4])
        operation_prompt = int(user_input[0])
        if operation_prompt in range(len(operations)):
            print(operations[operation_prompt](a,b))
        else:
            print('Invalid Choice')
    except (ValueError, IndexError):
        print("Error: Invalid input format. Please follow the correct format: [Input Prompt](input1,input2)")
    input_ques()
    

input_ques()
