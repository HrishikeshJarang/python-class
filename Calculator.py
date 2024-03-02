#def my_function(var1, var2)
#Calculator
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

#Add
def add(n1, n2):
    return n1 + n2

#Substract
def sub(n1, n2):
    return n1 - n2

#Multiplication
def mul(n1, n2):
    return n1 * n2

# #Division
def div(n1, n2):
    return n1 / n2

#Dictionary
operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def calculator():   #Recursion
    print(logo)
    num1 = float(input("Enter first number - "))
    for symbols in operations:    #all operations store in symbols variable
        print(symbols)  #show all symbols which present in operations
        
    should_continue = True
    while should_continue:
        operations_symbols = operations[symbols]  #variable operations_symbols = operations[symbols] = +, -, *, /
        operations_symbols = input("Pick the operation - ") 
        num2 = float(input("Enter second number - ")) 
        calculation_function = operations[operations_symbols] #Whatever function i have ("+" or "-" or "*" or "/") choose that function gets called from operations dictionary
        #Retrieves the function corresponding to the selected operation from the operations dictionary and stores it in the variable calculation_function.
        answer = calculation_function(num1, num2)
        #Calls the selected calculation function (add, sub, mul, or div) with num1 and num2 as arguments, and stores the result in the variable answer
        print(f"{answer}")

        if input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer  #should confirm that num1 = answer for continue
        else:
            should_continue = False
            calculator()  #After type 'n' again it goes back to start from "num1" i.e. it reset again    


calculator()

