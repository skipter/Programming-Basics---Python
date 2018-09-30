numberOfStars = int(input())

for i in range (numberOfStars):
    print("*", end = "")
    for x in range (numberOfStars - 1):
        print(" *", end = "")
    print()