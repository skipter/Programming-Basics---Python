badGradesCount = int(input())

numberOfProblems = 0
numOfBadGrades = 0
gradeScore = 0.0
problemName = None

while badGradesCount != numOfBadGrades:
    command = input()
    if command == "Enough":
        break
    grade = int(input())
    if grade <= 4:
        numOfBadGrades += 1

    gradeScore += grade
    numberOfProblems += 1
    problemName = command

if badGradesCount == numOfBadGrades:
    print(f"You need a break, {badGradesCount} poor grades.")
else:
    print(f'Average score: {(gradeScore / numberOfProblems):.2f}')
    print(f"Number of problems: {numberOfProblems}")
    print(f"Last problem: {problemName}")