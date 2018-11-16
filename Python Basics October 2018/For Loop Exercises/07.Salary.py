facebook = 150
instagram = 100
reddit = 50

number_of_open_tabs = int(input())
salary = int(input())
n = number_of_open_tabs
ouput = "You have lost your salary."
while n > 0:

    currentSite = input()

    if currentSite == "Facebook":
        salary -= facebook
        if salary <= 0:
            print(ouput)
            break
    elif currentSite == "Instagram":
        salary -= instagram
        if salary <= 0:
            print(ouput)
            break
    elif currentSite == "Reddit":
        salary -= reddit
        if salary <= 0:
            print(ouput)
            break
    n -= 1
if salary > 0:
    print(salary)

