count = int(input())

if count <= 4:
    print(f"/{'^' * (count // 2)}\/{'^' * (count // 2)}\\")
else:
    print(f"/{'^' * (count // 2)}\{'_' * (count * 2 - 4 - 2 * (count // 2))}/{'^' * (count // 2)}\\")

if count > 4:
    for x in range(count - 3):
        print(f"|{' ' * (count * 2 - 2)}|")
    print(f"|{' ' * (count // 2 + 1)}{'_' * (count * 2 - 4 - 2 * (count // 2))}{' ' * (count // 2 + 1)}|")
    print(f"\{'_' * (count // 2 )}/{' ' * (count * 2 - 4 - 2 * (count // 2))}\{'_' * (count // 2)}/")
else:
    for x in range(count - 2):
        print(f"|{' ' * (count * 2 - 2)}|")
    print(f"\{'_' * (count // 2)}/\{'_' * (count // 2)}/")