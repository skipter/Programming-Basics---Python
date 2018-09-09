firstNum = int(input())
secondNum = int(input())
thurdNum = int(input())

totalSum = firstNum + secondNum + thurdNum

minutes = 0;
seconds = 0;

if totalSum > 0 and totalSum <  59:
    minutes = 0
    seconds = totalSum
elif totalSum >= 60 and totalSum <= 119:
    minutes = 1
    seconds = totalSum - minutes * 60
elif totalSum > 120 and totalSum < 179:
    minutes = 2
    seconds = totalSum - minutes * 60

print("%0d:%02d" % (minutes, seconds))

