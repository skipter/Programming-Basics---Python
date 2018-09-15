import math

figure = input()

if figure == 'square':
    lenght = float(input())
    area = lenght * lenght
    print("{0:.03f}".format(area))

elif figure == 'rectangle':
    lenght1 = float(input())
    lenght2 = float(input())
    area = lenght1 * lenght2
    print("{0:.03f}".format(area))

elif figure == 'circle':
    r = float(input())
    area = r * r * math.pi
    print("{0:.03f}".format(area))

elif figure == 'triangle':
    lenght = float(input())
    h = float(input())
    area = lenght * h / 2
    print("{0:.03f}".format(area))

