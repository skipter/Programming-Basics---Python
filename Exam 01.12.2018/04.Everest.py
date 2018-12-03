day_counter = 1
everest = 8848
progress = 5364
command = input()

while command != "END":

    if command == "Yes":
        day_counter += 1

        if day_counter > 5:
            break

    meters = int(input())
    progress += meters

    if progress >= everest:
        break
    command = input()

if progress >= everest:
    print(f"Goal reached for {day_counter} days!")
else:
    print(f"Failed!")
    print(f"{progress}")
