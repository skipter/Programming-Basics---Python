month = input()
nights = int(input())

discountStudio = 0
discountFlat = 0

if month == "May" or month == "October":
    studio = 50 * nights
    flat = 65 * nights
    discountFlat = flat
    discountStudio = studio
    if nights > 7 and nights < 14:
        discountStudio = studio - studio * 5 / 100

    elif nights >= 14:
        discountStudio = studio - studio * 30 / 100
        discountFlat = flat - flat * 10 / 100

elif month == "June" or month == "September":
    studio = 75.20 * nights
    flat = 68.70 * nights

    discountFlat = flat
    discountStudio = studio

    if nights > 14:
        discountStudio = studio - studio * 20 / 100
        discountFlat = flat - flat * 10 / 100

elif month == "July" or month == "August":
    studio = 76 * nights
    flat = 77 * nights
    discountStudio = studio
    discountFlat = flat

    if nights > 14:
        discountFlat = flat - flat * 10 / 100


print(f"Apartment: {discountFlat:.2f} lv.")
print(f"Studio: {discountStudio:.2f} lv.")