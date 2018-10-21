import math
a = float(input())
b = float(input())
c = float(input())
d = float(input())

totalTime = 1 / (1/a + 1/b + 1/c)
totalTime = totalTime + totalTime * 0.15
d = d - totalTime

if d >= 0:
    print(f"Cleaning time: {totalTime:.2f}")
    print(f"Yes, there is a surprise - time left -> {math.floor(d)} hours.")
else:
    print(f"Cleaning time: {totalTime:.2f}")
    print(f"No, there isn't a surprise - shortage of time -> {math.ceil((abs(d)))} hours.")
