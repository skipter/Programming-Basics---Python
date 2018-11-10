import math
money = float(input()) * 100
rest = 0.0
coins = 0.0


while money > 0:

    rest = money % 200
    coins += math.floor(money / 200)
    money = money - coins * 200


    money = rest
    rest = money % 100
    coins += math.floor(money / 100)
    money = money - coins * 100


    money = rest
    rest = money % 50
    coins += math.floor(money / 50)
    money = money - coins * 50


    money = rest
    rest = money % 20
    coins += math.floor(money / 20)
    money = money - coins * 20


    money = rest
    rest = money % 10
    coins += math.floor(money / 10)
    money = money - coins * 10

    money = rest
    rest = money % 5
    coins += math.floor(money / 5)
    money = money - coins * 5


    money = rest
    rest = money % 2
    coins += math.floor(money / 2)
    money = money - coins * 2


    money = rest
    rest = money % 1
    coins += math.floor(money / 1)
    money = money - coins * 1

    print(str(coins).rstrip('0').rstrip('.'))