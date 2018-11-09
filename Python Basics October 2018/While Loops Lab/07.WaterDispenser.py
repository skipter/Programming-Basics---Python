volume = int(input())
water = 0
counter = 0
while True:

    inputArgs = input()

    if inputArgs == "Easy":
        water += 50
    elif inputArgs == "Medium":
        water += 100
    elif inputArgs == "Hard":
        water += 200

    counter += 1

    if water == volume:
        print(f"The dispenser has been tapped {counter} times.")
        break
    elif water > volume:
        overFlow = water - volume
        print(f"{overFlow}ml has been spilled.")
        break