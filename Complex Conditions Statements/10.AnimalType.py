entity = input()

def typeOFAnimal (agrument):

    switcher = {
        "dog": "mammal",
        "snake": "reptile",
        "tortoise": "reptile",
        "crocodile": "reptile",
    }
    return switcher.get(agrument, "unknown")

print(typeOFAnimal(entity))