h = float(input())
w = float(input())

heightInSm = int((h * 100) / 120)
weight = (w * 100) - 100
weightWorkSections = int(weight / 70)

workPlaces = (heightInSm * weightWorkSections)
remove = 3;
print(workPlaces - remove)
