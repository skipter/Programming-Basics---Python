numbersCount = int(input())

p1 = 0
p2 = 0
p3 = 0

if numbersCount >= 1 and numbersCount <= 1000:
    for x in range(numbersCount):
        currentNum = int(input())

        if currentNum % 2 == 0:
            p1 += 1
        if currentNum % 3 == 0:
            p2 += 1
        if currentNum % 4 == 0:
            p3 += 1
else:
    numbersCount = int(input())

print(f"{p1 / numbersCount * 100:.2f}%")
print(f"{p2 / numbersCount * 100:.2f}%")
print(f"{p3 / numbersCount * 100:.2f}%")




