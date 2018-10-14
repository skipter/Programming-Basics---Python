whiskyPriceInBgn = float(input())
beerLiters = float(input())
wineLiters = float(input())
rakiaLiters = float(input())
whiskyLiters = float(input())

rakiaPrice = whiskyPriceInBgn / 2
winePrice = rakiaPrice - (0.4 * rakiaPrice)
beerPrice = rakiaPrice - (0.8 * rakiaPrice)

totalSum = (whiskyPriceInBgn * whiskyLiters) + (beerLiters * beerPrice) + (wineLiters * winePrice) + (rakiaPrice * rakiaLiters)
print(f"{totalSum:.2f}")