pricePerKgVegetables = float(input())
pricePerKgFruits = float(input())
kgVegetables = int(input())
kgFruits = int(input())

euroValue = 1.94

totalVegetables = pricePerKgVegetables * kgVegetables
totalFruits = pricePerKgFruits * kgFruits
totalBGN = totalFruits + totalVegetables
totalEuro = totalBGN / euroValue
print(totalEuro)