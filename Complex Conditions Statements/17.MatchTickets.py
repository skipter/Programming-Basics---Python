budget = float(input())
type = input()
peopleCOunt = int(input())

moneyLeft = 0

if peopleCOunt >= 1 and peopleCOunt <= 4:
    moneyForTransport = budget - budget * 75 / 100

elif peopleCOunt >= 5 and peopleCOunt <= 9:
    moneyForTransport = budget - budget * 60 / 100

elif peopleCOunt >= 10 and peopleCOunt <=24:
    moneyForTransport = budget - budget * 50 / 100

elif peopleCOunt >= 25 and peopleCOunt <= 49:
    moneyForTransport = budget - budget * 40 / 100

elif peopleCOunt >= 50:
    moneyForTransport = budget - budget * 25 / 100

price = 0
if type == "VIP":
    price = 499.99
else:
    price = 249.99
tickets = peopleCOunt * price
diff = moneyForTransport - tickets

if diff > 0:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print("Not enough money! You need {0:.02f} leva.".format(abs(diff)))
