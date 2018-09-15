num = int(input())

print(f"{'*' * (num * 2)}{' ' * (num)}{'*' * (num * 2)}")

for x in range(num - 2):
    if x == (num - 1) // 2 - 1:
        print(f"*{'/' * (num * 2 - 2)}*{'|' * num}*{'/' * (num * 2 - 2)}*")
    else:
        print(f"*{'/' * (num * 2 - 2)}*{' ' * num}*{'/' * (num * 2 - 2)}*")
print(f"{'*' * (num * 2)}{' ' * (num)}{'*' * (num * 2)}")