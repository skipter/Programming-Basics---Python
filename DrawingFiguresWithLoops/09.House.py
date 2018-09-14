num = int(input())

for i in range((num + 1) // 2):
    if i == 0:
        if num % 2 == 0:
            print(f"{'-' * ((num - 2) // 2)}**{'-' * ((num - 2) // 2)}")
        else:
            print(f"{'-' * ((num - 1) // 2)}*{'-' * ((num - 1) // 2)}")
    else:
        if num % 2 == 0:
            print(f"{'-' * ((num - (i+1) * 2) // 2)}{'*' * ((i+ 1) * 2)}{'-' * ((num - (i+1) * 2) // 2)}")
        else:
            print(f"{'-' * ((num + 1 - (i+1) * 2) // 2)}{'*' * ((i+ 1) * 2 - 1)}{'-' * ((num + 1 - (i+1) * 2) // 2)}")
            
for x in range (num // 2):
    print(f"|{'*' * (num - 2)}|")