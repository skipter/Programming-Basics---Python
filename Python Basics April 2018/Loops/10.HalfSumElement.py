numbersCount = int(input())

totalSum = 0
biggest = 0
for i in range (numbersCount):
    currentNumber = int(input())
    totalSum += currentNumber
    if currentNumber >= biggest:
        biggest = currentNumber

result = abs(totalSum - biggest)
diff = abs(result - biggest)

if result == biggest:
    print(f"Yes Sum = {result}")
else:
    print(f"No Diff = {diff}")