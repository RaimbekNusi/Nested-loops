"Raimbek Nussipkhozhin, NFU892, 11313819, Jeffrey Long"
import random as random
g = int(input("How many enemies are there?: "))
gengar_attack = [1, 2, 3]
HP = 35
while HP > 0 and g != 0:
    gac = random.random()
    pac = random.random()
    if gac > 0.5:
        ga = random.choice(gengar_attack)
        HP = HP - ga
        print("Gengar hits Pikachu and deals " + str(ga) + " damage!")
        pac = random.random()
        if pac > 0.6:
            print("Pikachu hits Gengar and defeats him!")
            g = g - 1
    elif pac > 0.6:
        print("Pikachu hits Gengar and defeats him!")
        g = g - 1
if HP <= 0:
    print("Oh no! Pikachu fainted!")
if g == 0:
    print("Pikachu defeated all the Gengars!")
    print("He has " + str(HP) + " HP left!")
