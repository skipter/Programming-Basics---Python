x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

isOnTop = ((x >= x1 and x <= x2) and (y == y1))
isOnBottom = ((x >= x1 and x <= x2) and (y == y2))
isOnLeftSide = (y >= y1 and y <= y2) and x == x1
isOnRightSide = (y >= y1 and y <= y2) and x == x2
isOnBorder = (isOnTop or isOnBottom or isOnLeftSide or isOnRightSide);
if isOnBorder:
    print("Border")
else:
     print("Inside / Outside")