fruit_type = input()
set_type = input()
set_count = int(input())
price = None
if set_type == "small":
    if fruit_type == "Watermelon":
        price = 2 * 56
    elif fruit_type == "Mango":
        price = 2 * 36.66
    elif fruit_type == "Pineapple":
        price = 2 * 42.10
    elif fruit_type == "Raspberry":
        price = 2 * 20
elif set_type == "big":
    if fruit_type == "Watermelon":
        price = 5 * 28.70
    elif fruit_type == "Mango":
        price = 5 * 19.60
    elif fruit_type == "Pineapple":
        price = 5 * 24.80
    elif fruit_type == "Raspberry":
        price = 5 * 15.20

total_value = price * set_count

if total_value >= 400 and total_value <= 1000:
    total_value = total_value - (total_value * 0.15)
elif total_value > 1000:
    total_value = total_value - (total_value * 0.50)

print(f"{total_value:.2f} lv.")



