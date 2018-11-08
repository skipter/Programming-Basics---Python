name = input()

years = 1
sum = 0.0

while years <= 12:
    grade = float(input())

    if grade >= 4:
        sum += grade
        years += 1

average = sum / 12

print(f"{name} graduated. Average grade: {average:.2f}")
