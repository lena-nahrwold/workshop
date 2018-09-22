print()

print("What is your name?")

name = input("> ")

print(f"Welcome to the Dungeon, {name}!")
print("Do you go through door 1 or door 2?")

door = input("> ")

if door == "1":
    print("There is a nice vampire asking you if you enjoy life.")
    print("What do you do?")
    print("1. Smile and nod")
    print("2. Scream and run")

    vampire = input("> ")

    if vampire == "1":
        print(f"Congratulations {name}, you found a new friend!")

    elif vampire == "2":
        print(f"Sorry {name}, the vampire is faster. You become a dinner.")

    else:
        print("You are not so good with numbers, are you?")

if door == "2":
    print("There are two vampires staring at you. One of them asks you, if you are hungry.")
    print("What do you do?")
    print("1. Say Yes and smile")
    print("2. Say No and run")

    vampire = input("> ")

    if vampire == "1":
        print(f"Guten Appetit {name}, you have dinner with your new friends.")

    elif vampire == "2":
        print(f"Oops, you are a delicious dinner for vampires, {name}.")

    else:
        print("You are not so good with numbers, are you?")


print(f"Did you enjoy your visit in the Dungeon, {name}?")
print("1. Yes, I made new friends.")
print("2. No, I died in here.")

answer = input("> ")

if answer == "1":
    print(f"Great, we are looking forward to welcome you again, {name}!")

elif answer == "2":
    print(f"Sorry {name}, rest in peace.")

else:
    print("You are not so good with numbers, are you?")
