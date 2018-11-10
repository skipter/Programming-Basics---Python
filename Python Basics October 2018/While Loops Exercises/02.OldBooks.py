bookToLookFor = input()
libraryCount = int(input())
startCount = libraryCount
counter = 0
isFound = False
while libraryCount > 0:

    currentBook = input()
    if currentBook == bookToLookFor:
        print(f"You checked {counter} books and found it.")
        break
    counter += 1
    libraryCount -= 1

if libraryCount == 0:
    print(f"The book you search is not here!")
    print(f"You checked {startCount} books.")