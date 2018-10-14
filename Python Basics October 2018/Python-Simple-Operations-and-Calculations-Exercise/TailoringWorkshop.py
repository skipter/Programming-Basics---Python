tableCount = int(input())
length = float(input())
width = float(input())

dollarValue = 1.85
rectangleCover = 7
squareCover = 9

currentRectangleCover = tableCount * (length + 2 * 0.30) * (width + 2 * 0.30)
currentSquareCover = tableCount * (length / 2) * (length / 2)

priceInDollars = currentRectangleCover * rectangleCover + currentSquareCover * squareCover
priceInBg = priceInDollars * dollarValue

print(f"{priceInDollars:.2f} USD")
print(f"{priceInBg:.2f} BGN")
