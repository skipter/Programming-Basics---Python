budget = float(input())
season = input()

sleeps = None
destination = None

#In Bulgaria - (Summer - Camp 30% or winter - hotel 70%)
if budget <= 100 and budget > 0:
    destination = "Bulgaria"
    if season == "summer":
        sleeps = "Camp"
        spend = budget - budget * 30 / 100
        money = budget - spend
    else:
        sleeps = "Hotel"
        spend = budget - budget * 70 / 100
        money = budget - spend

#In Balkans - (Summer - Camp 40% or winter - hotel 80%)
elif budget > 100 and budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        sleeps = "Camp"
        spend = budget - budget * 40 / 100
        money = budget - spend
    else:
        sleeps = "Hotel"
        spend = budget - budget * 80 / 100
        money = budget - spend

#In Europe - Hotel (90% budget and hotel)
elif budget > 1000:
    destination = "Europe"
    sleeps = "Hotel"
    spend = budget - budget * 90 / 100
    money = budget - spend

print(f"Somewhere in {destination}")
print(f"{sleeps} - {money:.2f}")