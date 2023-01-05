#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu

# Date: Jan. 4, 2022
# a calculator program


def calculate(sign, num1, num2):
    # addition
    if sign == "+":
        answer = num1 + num2

    # subtraction
    elif sign == "-":
        answer = num1 - num2

    # multiplication
    elif sign == "*":
        answer = num1 * num2

    # division
    elif sign == "/":
        answer = num1 / num2

    # modulus
    elif sign == "%":
        answer = num1 % num2

    # invalid sign
    else:
        return "invalid"

    return str(answer)


def main():
    # opening message
    print("This program does a calculation between 2 numbers. The operands")
    print("you can use are +, -, *, /, and %.")

    # getting user input for the sign
    user_sign = input("Enter the operand: ")

    # getting user input for the first number
    first_num_str = input("Enter the first number: ")

    # getting user input for the second number
    second_num_str = input("Enter the second number: ")

    # exception handling
    try:
        # casting the number inputs
        first_num_fl = float(first_num_str)
        second_num_fl = float(second_num_str)

    # input is invalid
    except Exception:
        # exception message
        print("Please make sure the numbers you imputed are valid.")

    # input is valid
    else:
        #  calls the function to do the calculation
        result = calculate(user_sign, first_num_fl, second_num_fl)

        # displays the results
        if result == "invalid":
            print(f"The result of {first_num_fl} {user_sign} {second_num_fl} is {result}.")
        else:
            print(f"The result of {first_num_fl} {user_sign} {second_num_fl} is {int(result):.2f}.")

if __name__ == "__main__":
    main()
