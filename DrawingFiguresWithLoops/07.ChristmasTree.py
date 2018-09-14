num = int(input())

for i in range(num + 1):
    print(f"{' ' * (num - i)}{'*' * (i)} | {'*' * (i)}")