budget = int(input())
season = input()
fishersCount = int(input())
boatPrice = 0

if season == "Winter":
    boatPrice = 2600
elif season == "Spring":
    boatPrice = 3000
else:
    boatPrice = 4200

if fishersCount <= 6:
    boatPrice = boatPrice - boatPrice * 0.10
elif fishersCount > 6 and fishersCount <= 11:
    boatPrice = boatPrice - boatPrice * 0.15
elif fishersCount > 11:
    boatPrice = boatPrice - boatPrice * 0.25

if fishersCount % 2 == 0 and season != "Autumn":
    boatPrice = boatPrice - boatPrice * 0.05

if budget >= boatPrice:
    budget = budget - boatPrice
    print(f"Yes! You have {budget:.2f} leva left.")
else:
    diff = abs(budget - boatPrice)
    print(f"Not enough money! You need {diff:.2f} leva.")