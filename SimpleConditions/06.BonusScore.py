number = int(input())
#TODO correct the logic, there is a mistake with calculations.
if number <= 100:
    number += 5
elif number > 100:
    currentNum = number - number * 20 / 100
    number = currentNum
elif number > 1000:
    currentNum = number - number * 20 / 100
    number = currentNum

if number % 2 == 0:
    number += 1
if number % 10 == 5:
    number += 2

print(number)