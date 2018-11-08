number = input()
maxNum = -999999999999999999999
minNum = 999999999999999999999
while not number == "END":
    number = int(number)

    if number >= maxNum:
        maxNum = number

    if number <= minNum:
        minNum = number

    number = input()

print(f"Max number: {maxNum}")
print(f"Min number: {minNum}")




