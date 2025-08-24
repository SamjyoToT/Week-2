name = input("Naam ke ho?: ")
age = int(input("Budhapa ko mulyankan: "))

def make_card(name, age, message = "Rom Rom bhaiyo"):
    return f"Namaste {name}, ({age} Budho)!\n{message}"

print(make_card(name, age))
