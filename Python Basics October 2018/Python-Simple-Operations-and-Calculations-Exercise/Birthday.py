length = int(input())
width = int(input())
height = int(input())
procent = float(input())

volume = (height * width * length) * 0.001
procent = procent * 0.01

result = volume * (1 - procent)
print(f"{result:.3f}")
