needed_money = float(input())
current_money = float(input())
day_counter = 0
spending_counter = 0

while needed_money > current_money:
    command = input()
    money = float(input())
    if command == "spend":
        current_money -= money
        spending_counter += 1
        if current_money < 0:
            current_money = 0
    elif command == "save":
        current_money += money
        spending_counter = 0
    day_counter += 1
    if spending_counter == 5:
        break;

if needed_money <= current_money:
    print(f"You saved the money for {day_counter} days.")
else:
    print(f"You can't save the money.")
    print(day_counter)
