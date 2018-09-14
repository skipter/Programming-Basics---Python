n = int(input())

print(f"{'.' * (n + 1)}{'_' * (n * 2 + 1)}{'.' * (n + 1)}")

for x in range(n - 1):
    print(f"{'.' * (n - x)}//{'_' * (n + 2 + x)}\\\\{'.' * (n - x)}")
print(f"{'.' * (n - x)}//{'_' * (n * 3)}\\\\{'.' * (n - x)}")

#ToDo correct logic