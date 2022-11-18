# My calculator
def calculator():
    num1 = float(input("Enter one number: "))
    op = input("Enter operator: ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        return num1 + num2
    elif op == "-":
        if num1 >= num2:
            return num1 - num2
        else:
            return num2 - num1
    elif op == "/":
        return num1 / num2
    elif op == "*":
        return num1 * num2
    else:
        return "Invalid operator"


print(calculator())
