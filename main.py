# Author : BEGUE Laurier

# Importation des bibliothèques
from src import func as f
from src import quadraticEquation as qe
from src import FDEquation as fde


def menu():
    f.clear()
    print(
        """
            Bienvenue dans le programme de résolution d'équation
[1] Second degré
[2] Premier degré
[3] Quitter
"""
    )


# Programme principal
if __name__ == "__main__":
    while True:
        try:
            menu()
            choice = int(input("Votre choix: "))
            if choice == 1:
                qe.runQE()
            elif choice == 2:
                fde.runEFD()
            elif choice == 3:
                f.clear()
                print("Au revoir")
                break
            else:
                menu()
        except ValueError:
            menu()
