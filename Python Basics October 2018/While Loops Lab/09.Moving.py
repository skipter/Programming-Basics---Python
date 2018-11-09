width = int(input())
lenght = int(input())
height = int(input())

roomVolume = width * lenght * height
volumeIncome = 0

command = input()
while command != "Done":

    currentVolume = int(command)
    volumeIncome += currentVolume

    if volumeIncome > roomVolume:
        diff = volumeIncome - roomVolume
        print(f"No more free space! You need {diff} Cubic meters more.")
        break

    command = input()
    if command == "Done":
        diff = roomVolume - volumeIncome
        print(f"{diff} Cubic meters left.")


