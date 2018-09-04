value = float(input())
inputCurrency = input()
outputCurrency = input()

convert = 0;
if inputCurrency=='USD':
    convert = 1.79549 * value
elif inputCurrency=='EUR':
    convert = 1.95583 * value
elif inputCurrency=='GBP':
    convert = 2.53405 * value

#TODO Correct the logic and finish the exercise.






#print("{0:.02f}".format(resultValue))