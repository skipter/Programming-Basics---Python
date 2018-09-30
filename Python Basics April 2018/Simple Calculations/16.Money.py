bitcoinsCount = int(input())
chainessIuna = float(input())
tax = float(input())

bitcoinValue = 1168
iuna = 0.15 #usd
usd = 1.76
euro = 1.95

totalBitcoinsValue = bitcoinsCount * bitcoinValue
totalIunis = iuna * chainessIuna
usdToBgn = totalIunis * usd
totalBGN = totalBitcoinsValue + usdToBgn
totalEURO = totalBGN / euro

total = totalEURO - totalEURO * tax / 100

print("{0:.02f}".format(total))