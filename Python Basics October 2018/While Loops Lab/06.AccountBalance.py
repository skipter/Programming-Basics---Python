numberOFTransaction = int(input())
totalSum = 0.0
while numberOFTransaction > 0:

    value = float(input())
    if value < 0:
        print("Invalid operation!")

        break
        print(f"Total: {totalSum:.2f}")
    else:
        totalSum += value
        print(f"Increase: {value:.2f}")
    numberOFTransaction -= 1

print(f"Total: {totalSum:.2f}")