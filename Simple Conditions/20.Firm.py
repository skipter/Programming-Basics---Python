import math

neededHours = int(input())
daysToWork = int(input())
hardWorkingPeople = int(input())

workersLearning = daysToWork - daysToWork * 10 / 100

workingHours = workersLearning * 8

overtime = math.floor(hardWorkingPeople * 2 * daysToWork)
totalHours = math.floor(workingHours + overtime)
diff = abs(totalHours - neededHours)

if totalHours > neededHours:
    print(f"Yes!{diff} hours left.")
else:
    print(f"Not enough time!{diff} hours needed.")

