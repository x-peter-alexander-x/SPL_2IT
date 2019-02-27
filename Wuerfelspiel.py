import random

random.seed

anzahlRunden = input("Wie viele Runden?")
userEingabe = input("Welche Zahl?")
counterR = 0
counterW = 0

for i in range(int(anzahlRunden)):
    rZ = random.randint(1, 6)
    if(rZ==int(userEingabe)):
       counterR=counterR+1
    else:
        counterW=counterW+1
    if(counterW>=7):
        print("Verloren",userEingabe,"wurde nur",counterR,"x gezogen")
        break

    if(int(userEingabe)==rZ):
        print("*"+userEingabe+"*")
    else:
        print(rZ)

print(counterW)
print(counterR)
