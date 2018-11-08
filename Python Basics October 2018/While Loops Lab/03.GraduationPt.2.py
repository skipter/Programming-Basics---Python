name = input()

years = 1
sum = 0.0
isExcluded = False
while years <= 12:
    grade = float(input())

    if grade >= 4:
        sum += grade
        years += 1
    else:
        print(f"{name} has been excluded at {years} grade")
        isExcluded = True
        break

average = sum / 12
if (isExcluded == False):
    print(f"{name} graduated. Average grade: {average:.2f}")
