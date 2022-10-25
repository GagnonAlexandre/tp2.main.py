# TP2
# Alexandre Gagnon
from random import *


def jeu():
    jeu_commence = True #voir le commentaire en bas
    print("Bienvenue au jeu de devinette! Commencer par écrire la limite des nombres puis commence a deviner!")

    while jeu_commence:
        limite_1 = int(input("Entrez la limite pour le plus petit nombre:"))
        limite_2 = int(input("Entrez la limite pour le plus gros nombre:"))
        nb_essais = 1
        nombre_mystere = randint(limite_1, limite_2) #je creer une fonction ou le nombre mystere vas etre choisie entre les deux limites

        not_found = True
        while not_found:
            essai = int(input("Entrez votre essai:"))
            if essai < limite_1:
                print("Votre nombre dépasse la limite")
            elif essai > limite_2:
                print("Votre nombre dépasse la limite")
            elif essai > nombre_mystere:
                print("Le numero est plus petit")
                nb_essais += 1
            elif essai < nombre_mystere:
                print("Le numero est plus grand")
                nb_essais += 1
            else:
                print(f"Bravo! Vous avez devinez le numéro en {nb_essais} essaies.")
                not_found = False
                restart = input("Si vous voulez rejouer, tapez (o). Sinon, tapez (n)")
                if restart == "o":
                    jeu_commence = True
                elif restart == "n":
                    print("A la prochaine!")
                    jeu_commence = False


jeu()
#jeu_commence = True est le demarage officiel du jeux se qui apres avoir fini le jeux peux permet de recommencer et de faire une boucle
#les lignes 29 a 37 permet de savoir quand le joueur a gagner en combien dessay et permet au joueur de continuer ou darreter