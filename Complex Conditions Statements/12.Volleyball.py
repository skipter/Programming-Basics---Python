import math

typeOfYear = input()
holidays = int(input())
weekendsInHometown = int(input())

weekendsInSofia = 48 - weekendsInHometown
diff = weekendsInSofia - weekendsInSofia * 75 / 100
saturdayGamesInSofia = weekendsInSofia - diff

hollidayGames = holidays - holidays * 2/3
hollidayGames1 = holidays - hollidayGames

totalGames = weekendsInHometown + saturdayGamesInSofia + hollidayGames1

if typeOfYear == "leap":
   totalGames *= 1.15

print(math.floor(totalGames))

