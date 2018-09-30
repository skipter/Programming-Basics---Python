numbersCount = int(input())
oddSum = 0
evenSum = 0
for i in range(numbersCount):
    currentNum = int(input())
    if i % 2 == 0:
        evenSum += currentNum
    else:
        oddSum += currentNum

diff = abs(oddSum - evenSum)

if oddSum == evenSum:
    print(f"Yes Sum = {oddSum}")
else:
    print(f"No diff = {diff} ")