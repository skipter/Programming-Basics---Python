import math

area = int(input())
grapePerM = float(input())
needWine = int(input())
workers = int(input())

totalGrape = area * grapePerM
wine = totalGrape - totalGrape * 40 / 100
total = (totalGrape - wine) / 2.5

if total >= needWine:

    wineForWorkers = total - needWine
    winePerPerson = wineForWorkers / workers

    print(f"Good harvest this year! Total wine: {math.floor(int(total))} liters.")
    print(f"{math.ceil(total - needWine)} liters left -> {math.ceil(winePerPerson)} liters per person.")

else:
    math.floor(total)
    wineForWorkers = total - needWine
    winePerPerson = wineForWorkers / workers

    print(f"It will be a tough winter! More {math.floor(abs(wineForWorkers))} liters wine needed.")

