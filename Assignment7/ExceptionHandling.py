import sys

from Exceptions.UserDefinedException import FormulaError

while True:

    user_input = input("Enter the formula (format: a + b): ")
    if user_input == "quit":
        sys.exit()
    formula_list = list(user_input.split())
    try:
        if 2 < len(formula_list) > 2:
            raise FormulaError("Input should consist 3 elements")
        elif formula_list[1] != "+" and formula_list[1] != "-":
            raise FormulaError("Invalid operator")
        a = float(formula_list[0])
        b = float(formula_list[2])
        operator = formula_list[1]
        print("The calculation of given formula is:", end=" ")
        if operator == "+":
            print(a + b)
        else:
            print(a - b)

    except FormulaError as error:
        print(error.message)
    except ValueError as error:
        try:
            raise FormulaError(error)
        except FormulaError as error1:
            print(error1.message)
