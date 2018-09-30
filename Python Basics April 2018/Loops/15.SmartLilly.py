age = int(input())
price = float(input())
priceForSingleToy = int(input())

money = 0

for x in range (1, age + 1):

    if x % 2 == 1:
        money += priceForSingleToy
    else:
        money += x // 2 * 10 - 1

if money >= price:
    print(f"Yes! {(money - price):.2f}")
else:
    print(f"No! {(price - money):.2f}")
