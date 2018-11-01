flowerType = input()
flowerCount = int(input())
budget = int(input())

rose = 5
dahlias = 3.80
tulips = 2.80
narcissus = 3
gladiolus = 2.50

totalPrice = 0

if flowerType == "Roses":
    totalPrice = rose * flowerCount
    if flowerCount > 80:
        totalPrice = totalPrice - totalPrice * 0.10

elif flowerType == "Dahlias":
    totalPrice = dahlias * flowerCount
    if flowerCount > 90:
        totalPrice = totalPrice - totalPrice * 0.15

elif flowerType == "Tulips":
    totalPrice = tulips * flowerCount
    if flowerCount > 80:
        totalPrice = totalPrice - totalPrice * 0.15

elif flowerType == "Narcissus":
    totalPrice = narcissus * flowerCount
    if flowerCount < 120:
        totalPrice = totalPrice + totalPrice * 0.15


elif flowerType == "Gladiolus":
    totalPrice = gladiolus * flowerCount
    if flowerCount < 80:
        totalPrice = totalPrice + totalPrice * 0.20

if budget >= totalPrice:
    print(f"Hey, you have a great garden with {flowerCount} {flowerType} and {budget - totalPrice:.2f} leva left.")
else:
    diff = abs(budget - totalPrice)
    print(f"Not enough money, you need {diff:.2f} leva more.")