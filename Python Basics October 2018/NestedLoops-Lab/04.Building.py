floors = int(input())
rooms = int(input())

letter = None
for floor in range(floors, 0, -1):
    for room in range(0, rooms):

        if floor % 2 == 0:
            letter = 'O'
        else:
            letter = 'A'

        if floors == floor:
            letter = 'L'

        print(f"{letter}{floor}{room} ", end='')
    print()




