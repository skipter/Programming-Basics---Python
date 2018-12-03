key_number = int(input())

is_key_found = False

for x in range(1, 31):
    for i in range(1, 31):
        for j in range(1, 31):
            if x < i < j:
                if x + i + j == key_number:
                    is_key_found = True
                    print(f"{x} + {i} + {j} = {key_number}")
            if x > i > j:
                if x * i * j == key_number:
                    is_key_found = True
                    print(f"{x} * {i} * {j} = {key_number}")

if is_key_found == False:
    print("No!")
