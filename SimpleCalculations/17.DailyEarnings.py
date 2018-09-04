workingDays = int(input())
moneyPerDay = float(input())
USDtoLev = float(input())

monthFee = workingDays * moneyPerDay
yearFee = monthFee * 12 + monthFee * 2.5

clearMoneyUSD = yearFee - yearFee * 25 /100

totalClearMoney = clearMoneyUSD * USDtoLev
moneyWinPerDay = totalClearMoney / 365

print("{0:.02f}".format(moneyWinPerDay))