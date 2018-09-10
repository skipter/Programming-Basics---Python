typeOfYear = input()
holidays = int(input())
weekendsInHometown = int(input())

weekendsInSofia = 48 - weekendsInHometown
diff = weekendsInSofia - weekendsInSofia * 75 / 100
saturdayGamesInSofia = weekendsInSofia - diff
print(saturdayGamesInSofia)

hollidayGames = holidays - holidays

#ToDo to finish the logic.