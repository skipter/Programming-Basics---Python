kilometers = int(input())
timeOfTheDay = input()

list = []

taxPrice = 0;
if timeOfTheDay == 'day':
    taxPrice = 0.70 + 0.79 * kilometers
    list.append(taxPrice)
elif timeOfTheDay == 'night':
    taxPrice = 0.70 + 0.90 * kilometers
    list.append(taxPrice)

if kilometers >= 20 and kilometers < 100:
    busPrice = kilometers * 0.09
    list.append(busPrice)
elif kilometers >= 100:
    trainPrice = kilometers * 0.06
    list.append(trainPrice)
print("{0:.02f}".format(min(list)))