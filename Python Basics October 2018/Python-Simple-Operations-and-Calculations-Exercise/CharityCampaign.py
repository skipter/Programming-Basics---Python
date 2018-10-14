days = int(input())
bakersCount = int(input())
cakeCount = int(input())
gofrettiCount = int(input())
pancakesCount = int(input())

cake = 45
gofretta = 5.80
pancake = 3.20

totalCakes = cake * cakeCount
totalGofretti = gofretta * gofrettiCount
totalPancakes = pancake * pancakesCount

dayTotalMoney = ((totalCakes + totalGofretti + totalPancakes) * bakersCount) * days
diff = dayTotalMoney * 0.875
totalSum = dayTotalMoney - diff
result = dayTotalMoney - totalSum
print(f"{result:.2f}")