nonWorkingDays = int(input())

yearMinutesToPlay = nonWorkingDays * 127
workingDays = (365 - nonWorkingDays) * 63

totalMinutes = yearMinutesToPlay + workingDays

if totalMinutes >= 30000:
    totalMinutes = totalMinutes - 30000
    hours = totalMinutes // 60
    minutes = totalMinutes % 60

    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")

else:
    totalMinutes = 30000 - totalMinutes
    hours = totalMinutes // 60
    minutes = totalMinutes % 60
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")