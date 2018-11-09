steps = input()
totalSteps = 0

while totalSteps <= 10000:
    if steps != "Going home":
        steps = int(steps)
        totalSteps += steps
        if totalSteps >= 10000:
            print("Goal reached! Good job!")
            break

        steps = input()

    else:

        steps = input()
        steps = int(steps)
        totalSteps += steps

        if totalSteps < 10000:
            neededSteps = 10000 - totalSteps
            print(f"{neededSteps} more steps to reach goal.")
            break
        else:
            print("Goal reached! Good job!")
            break







