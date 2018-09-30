numberCOunt = int(input())
number = int(input())

for i in range (numberCOunt-1):
    currentNumber = int(input())

    if currentNumber < number:
        number = currentNumber
print(number)