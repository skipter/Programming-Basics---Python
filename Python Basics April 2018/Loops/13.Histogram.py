numbersCount = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for x in range (numbersCount):
    currentNumber = int(input())

    if currentNumber < 200:
        p1 += 1
    elif currentNumber >= 200 and currentNumber <= 399:
        p2 += 1
    elif currentNumber > 399 and currentNumber <= 599:
        p3 += 1
    elif currentNumber > 599 and currentNumber <= 799:
        p4 += 1
    elif currentNumber > 799:
        p5 += 1

print(f"{p1 / numbersCount * 100:.2f}%")
print(f"{p2 / numbersCount * 100:.2f}%")
print(f"{p3 / numbersCount * 100:.2f}%")
print(f"{p4 / numbersCount * 100:.2f}%")
print(f"{p5 / numbersCount * 100:.2f}%")