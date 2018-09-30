hour = int(input())
minutes = int(input())

min = minutes + 15

if min >= 60:
    min = min - 60
    hour = hour + 1

if hour > 23:
    hour -= 24

if min < 10:
    print("%0d:%02d" % (hour, min))
else:
    print("%0d:%02d" % (hour, min))
