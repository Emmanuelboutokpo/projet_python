import random
from random import *
NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = randint(NOMBRE_MIN,NOMBRE_MAX)
NMBRE_VIES = 4
def demander_nbre(nbre_min, nbre_max):
    result = 0
    while result == 0:
        res= input("Quel est le nombre magique (entre " + str(nbre_min)  + " et " + str(nbre_max) + ' ) ? ')
        try:
            result = int(res)
        except:
            print("ERREUR: Vous devez rentrer un nombre pour l’age")
        else :
            if result < nbre_min or result > nbre_max :
                print(f"ERREUR: Vous devez rentrer un nombre compris entre {nbre_min} et {nbre_max}")
                result = 0
    return  result
nbre=0
vie = 0
while (nbre != NOMBRE_MAGIQUE) and (vie !=NMBRE_VIES):
    print(f"Il vous reste {NMBRE_VIES-vie} vies")
    nbre = demander_nbre(NOMBRE_MIN, NOMBRE_MAX)
    if nbre==NOMBRE_MAGIQUE :
        print('Bravo, vous avez gagné !')
    elif nbre > NOMBRE_MAGIQUE :
            print('Le nombre magique est plus petit !')
    else:
            print('Le nombre magique est plus grand !')
    vie +=1
if vie == NMBRE_VIES :
    print(f"Vous avez perdu le nombre etait {NOMBRE_MAGIQUE}")