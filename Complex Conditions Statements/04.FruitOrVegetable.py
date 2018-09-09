text = input()

vetetables = ["tomato", "cucumber", "pepper ", "carrot", "pepper"]
fruits = ["apple", "kiwi", "cherry", "lemon", "grapes", "banana"]

if text in vetetables:
    print("vegetable")
elif text in fruits:
    print("fruit")
else:
    print("unknown")