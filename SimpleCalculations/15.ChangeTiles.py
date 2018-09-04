lengthFloor = float(input())
weightTile = float(input())
longTile = float(input())
benchWeight = float(input())
benchHeight = float(input())

totalFloorSize = lengthFloor * lengthFloor
benchTotalSize = benchHeight * benchWeight

floorForRecovery = totalFloorSize - benchTotalSize
tileArea = weightTile * longTile

neededTiles = floorForRecovery / tileArea
neededTime = neededTiles * 0.2
print(neededTiles)
print(neededTime)