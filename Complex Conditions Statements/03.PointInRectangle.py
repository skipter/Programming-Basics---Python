x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

xIsInside = x >= x1 and x <= x2
yIsInside = y >= y1 and y <= y2

if xIsInside and yIsInside:
    print("Inside")
else:
    print("Outside")

