temp = int(input())
dayTime = input()

outfit = ""
shoes = ""

if temp >= 10 and temp <= 18:
    if dayTime == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif dayTime == "Afternoon":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif dayTime == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif temp > 18 and temp <= 24:
    if dayTime == "Morning":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif dayTime == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif dayTime == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif temp >= 25:
    if dayTime == "Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif dayTime == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif dayTime == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {temp} degrees, get your {outfit} and {shoes}.")