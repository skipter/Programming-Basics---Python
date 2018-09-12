numbersCount = int(input())

oddSum = 0
evenSum = 0
oddMin = 1000000000.0
oddMax = 1000000000.0
evenMin = 1000000000.0
evenMax = 1000000000.0
if numbersCount == 0:
    print(f"OddSum={oddSum}, OddMin=No, OddMax=No, EvenSum={evenSum}, EvenMin=No, EvenMax=No")
else:
        #ToDo Correct the logic with max and printing result if it isnt zero counter.
    for i in range(1, numbersCount + 1):
        currentNumber = float(input())

        if i % 2 == 1:
            oddSum += currentNumber

            if currentNumber > oddMax:
                oddMax = currentNumber
            if currentNumber < oddMin:
                oddMin = currentNumber
        else:
            evenSum += currentNumber

            if currentNumber > evenMax:
                evenMax = currentNumber
            if currentNumber < evenMin:
                evenMin = currentNumber

    print(f"OddSum={oddSum:g},")
    if oddMin != None:
        print(f"OddMin={oddMin:g},")
    else:
        print("OddMin=No,")
    if oddMin != None:
        print(f"OddMax={oddMax:g},")
    else:
        print("OddMax=No,")

    print(f"EvenSum={evenSum:g},")
    if oddMin != None:
        print(f"EvenMin={evenMin:g},")
    else:
        print("EvenMin=No,")
    if oddMin != None:
        print(f"EvenMax={evenMax:g},")
    else:
        print("OddMax=No")
