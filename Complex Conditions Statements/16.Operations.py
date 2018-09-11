number1 = int(input())
number2 = int(input())
operand = input()

result = 0
whatIsTheNumber = None

if operand == "+":
    result = number1 + number2
    if result % 2 == 0:
        whatIsTheNumber = "even"
    else:
        whatIsTheNumber = "odd"
    print(f"{number1} {operand} {number2} = {result} - {whatIsTheNumber}")

elif operand == "-":
    result = number1 - number2
    if result % 2 == 0:
        whatIsTheNumber = "even"
    else:
        whatIsTheNumber = "odd"
    print(f"{number1} {operand} {number2} = {result} - {whatIsTheNumber}")

elif operand == "*":
    result = number1 * number2
    if result % 2 == 0:
        whatIsTheNumber = "even"
    else:
        whatIsTheNumber = "odd"
    print(f"{number1} {operand} {number2} = {result} - {whatIsTheNumber}")

elif operand == "/":
    if number2 == 0:
        print(f"Cannot divide {number1} by zero")
    else:
        result = number1 / number2
        print(f"{number1} {operand} {number2} = {result:.2f}")

elif operand == "%":
    if number2 == 0:
        print(f"Cannot divide {number1} by zero")
    else:
        result = number1 % number2
        print(f"{number1} {operand} {number2} = {result}")

