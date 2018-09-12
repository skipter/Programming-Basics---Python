numberCount = int(input())
leftSum = 0
rightSum = 0
for i in range(numberCount):
    currentNum = int(input())
    leftSum += currentNum
for x in range(numberCount):
    currentNum = int(input())
    rightSum += currentNum

result = abs(leftSum - rightSum)
temp = leftSum

if result == 0:
    print(f"Yes, sum = {temp}")
else:
    print(f"No, diff = {result}")
