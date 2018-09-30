count = int(input())

for x in range(0, count):
    print("$", end = "")
    for i in range(x):
        print(" $", end="")
    print()