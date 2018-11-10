width = int(input())
length = int(input())

cake_size = width * length
startValue = cake_size
command = input()
total = 0

while cake_size >= 0:

    if command == "STOP":
        break
    cake_size = cake_size - int(command)
    if cake_size < 0:
        break
    command = input()

if cake_size <= 0:
    print(f"No more cake left! You need {abs(cake_size)} pieces more.")
else:
    print(f"{cake_size} pieces are left.")
