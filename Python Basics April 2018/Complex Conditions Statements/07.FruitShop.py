fruit = input()
day = input()
quantity = float(input())

price = 0.00

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":

    fruits = {
    "banana":2.50,
    "apple":1.20,
    "orange":0.85,
    "grapefruit":1.45,
    "kiwi":2.70,
    "pineapple":5.50,
    "grapes": 3.85}

    if fruit in fruits:
        price = quantity * fruits[fruit]
        print("{0:.02f}".format(price))
    else:
        print("Error")

elif day == "Sunday" or day == "Saturday":

    holidayFruits = {
    "banana":2.70,
    "apple":1.25,
    "orange":0.90,
    "grapefruit":1.60,
    "kiwi":3.00,
    "pineapple":5.60,
    "grapes":4.20}

    if fruit in holidayFruits:
        price = quantity * holidayFruits[fruit]
        print("{0:.02f}".format(price))
    else:
        print("Error")
else:
    print("Error")