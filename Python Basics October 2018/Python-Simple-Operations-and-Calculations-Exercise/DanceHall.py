import math
l = float(input())
w = float(input())
a = float(input())

hallSize = (l * 100) * (w * 100)
wardrobeSize = (a * 100) * (a * 100)
benchSize = hallSize / 10
freeSpace = hallSize - wardrobeSize - benchSize
dancers = freeSpace / (40 + 7000)
print(math.floor(dancers))