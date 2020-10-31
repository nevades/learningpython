print("Welcome to the calculator built by Neva")
num1 = float(input("Enter the first number: "))
operator = input("Enter a operator: ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")

