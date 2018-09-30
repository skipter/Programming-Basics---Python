number = int(input())
# TODO correct the logic, there is a mistake with calculations.
tempNum = number
bonus = 0
if number <= 100:
    bonus += 5
    # number += 5
elif number > 100 and number < 1000:
    currentNum = number - number * 20 / 100
    temp = number - currentNum
    # number += temp
    bonus += temp
elif number > 1000:
    currentNum = number - number * 10 / 100
    temp = number - currentNum
    # number += temp
    bonus += temp

if tempNum % 2 == 0:
    # number += 1
    bonus += 1
if tempNum % 10 == 5:
    # number += 2
    bonus += 2

print(bonus)
print(number + bonus)
