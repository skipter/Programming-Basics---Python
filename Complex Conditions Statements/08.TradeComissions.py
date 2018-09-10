town = input()
sells = float(input())

comission = 0

if town == "Sofia":
    if sells < 0:
        print("error")
    elif sells >= 0 and sells <= 500:
        comission = sells - sells * 5 / 100
    elif sells > 500 and sells <= 1000:
        comission = sells - sells * 7 / 100
    elif sells > 1000 and sells <= 10000:
        comission = sells - sells * 8 / 100
    elif sells > 10000:
        comission = sells - sells * 12 / 100

    result = sells - comission
    print("{0:.02f}".format(result))

elif town == "Plovdiv":
    if sells < 0:
        print("error")
    elif sells >= 0 and sells <= 500:
        comission = sells - sells * 5.5 / 100
    elif sells > 500 and sells <= 1000:
        comission = sells - sells * 8 / 100
    elif sells > 1000 and sells <= 10000:
        comission = sells - sells * 12 / 100
    elif sells > 10000:
        comission = sells - sells * 14.5 / 100

    result = sells - comission
    print("{0:.02f}".format(result))

elif town == "Varna":
    if sells < 0:
        print("error")
    elif  sells >= 0 and sells <= 500:
        comission = sells - sells * 4.5 / 100
    elif sells > 500 and sells <= 1000:
        comission = sells - sells * 7.5 / 100
    elif sells > 1000 and sells <= 10000:
        comission = sells - sells * 10 / 100
    elif sells > 10000:
        comission = sells - sells * 13 / 100

    result = sells - comission
    print("{0:.02f}".format(result))
else:
    print("error")


