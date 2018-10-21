hollydayPrice = float(input())
puzzel = int(input())
barby = int(input())
bear = int(input())
minnion = int(input())
truck = int(input())

puzzelPrice = 2.60
barbyPrice = 3
bearPrice = 4.10
minnionPrice = 8.20
truckPrice = 2

totalToys = puzzel + barby + bear + minnion + truck
totalMOney = puzzel * puzzelPrice + barby * barbyPrice +\
             bear * bearPrice + minnion * minnionPrice + truck * truckPrice

if totalToys >= 50:
    totalMOney = totalMOney - totalMOney * 0.25

totalMOney = totalMOney - totalMOney * 0.10

endMoney = abs(totalMOney - hollydayPrice)

if totalMOney >= hollydayPrice:
    print(f"Yes! {endMoney:.2f} lv left.")
else:
    print(f"Not enough money! {endMoney:.2f} lv needed.")

