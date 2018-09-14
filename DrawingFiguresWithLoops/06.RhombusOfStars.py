num = int(input())

for i in range(1, num + 1):
    print((" " * ( num - i)), end="")
    print("*", end="")
    for x in range(i - 1):
        print(" *", end="")
    print()

for c in range(num - 1, 0, -1):
    print(" " * (num - c), end="")
    print("*",end="")
    for x in range(c - 1):
        print(" *", end="")

    print()