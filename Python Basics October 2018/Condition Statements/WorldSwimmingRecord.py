import math
record = float(input())
meters = float(input())
timePerMeter = float(input())

totalSecond = meters * timePerMeter
slowingSeconds = math.floor(meters / 15) * 12.5
totalSecond = totalSecond + slowingSeconds

if totalSecond < record:
    print(f"Yes, he succeeded! The new world record is {totalSecond:.2f} seconds.")
else:
    diff = abs(record - totalSecond)
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
