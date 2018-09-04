import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

x = abs(x1 - x2)
y = abs(y2 - y1)

area = x * y
perimeter = 2 * (x + y)
print(abs(area))
print(abs(perimeter))