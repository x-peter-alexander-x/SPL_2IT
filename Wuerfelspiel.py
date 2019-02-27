import random

random.seed

anzahlRunden = input("Wie viele Runden?")
userEingabe = input("Welche Zahl?")

for i in range(int(anzahlRunden)):
    rZ = random.randint(1, 6)
    if(rZ==int(userEingabe)):
        print("Winner!")
        break

    print(rZ)
