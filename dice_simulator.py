import random

while True:
    print(random.randint(1,6))
    a_roll=(input("do u wanna role again ? yes/no:"))
    if a_roll.lower()=="yes":
        continue
    else:
        break