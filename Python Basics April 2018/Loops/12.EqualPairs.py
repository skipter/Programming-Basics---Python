numberOfPairs = int(input())
firstCouple = int(input()) + int(input())

diff = 0

for x in range (numberOfPairs - 1):
    sum = int(input()) + int(input())

    if abs(firstCouple - sum) > diff:
        diff = abs(firstCouple - sum)

        firstCouple = sum
if diff == 0:
    print(f"Yes, value={firstCouple}")
else:
    print(f"No, maxdiff={diff}")