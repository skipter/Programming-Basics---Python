salary = float(input())
grade = float(input())
minimumSalary = float(input())

social = 0.35 * minimumSalary
scholar = grade * 25

if salary > minimumSalary and grade < 5.5:
    print("You cannot get a scholarship!")
elif salary < minimumSalary and grade < 4.5:
    print("You cannot get a scholarship!")
elif salary < minimumSalary and grade >= 4.5 and grade <= 5.5:
    print(f"You get a Social scholarship {int(social)} BGN")
elif salary < minimumSalary and grade >= 4.5 and social > scholar:
    print(f"You get a Social scholarship {int(social)} BGN")
elif salary < minimumSalary and grade >= 5.5 and scholar > social:
    print(f"You get a scholarship for excellent results {int(scholar)} BGN")
elif salary >= minimumSalary and grade >= 5.5:
    print(f"You get a scholarship for excellent results {int(scholar)} BGN")
