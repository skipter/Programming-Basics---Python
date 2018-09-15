n = int(input())

f = (n * 2) + (2 * n - 1) - 4

print(f"{'.' * (n + 1)}{'_' * (n * 2 + 1)}{'.' * (n + 1)}")

for x in range(n):
    print(f"{'.' * (n - x)}//{'_' * ((2 * n - 1) + x + x)}\\\\{'.' * (n - x)}")

print(f"//{'_' * (f // 2)}STOP!{'_' * (f // 2)}\\\\")


for i in range(n):
    print(f"{'.' * (i)}\\\\{'_' * ((f + 4) - i - i)}//{'.' * (i)}")