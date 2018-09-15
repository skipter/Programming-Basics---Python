n = int(input())

for x in range(n - 2):
    if x % 2 == 0:
        print(f"{'*' * (n - 2)}\ /{'*' * (n - 2)}")
    else:
        print(f"{'-' * (n - 2)}\ /{'-' * (n - 2)}")

print(f"{' ' * (n - 1)}@{' ' * (n - 1)}")

for x in range(n - 2):
    if x % 2 == 0:
        print(f"{'*' * (n - 2)}/ \{'*' * (n - 2)}")
    else:
        print(f"{'-' * (n - 2)}/ \{'-' * (n - 2)}")