import os
from src import quadraticEquation as qe


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def menu():
    clear()
    print(
        """
            Bienvenue dans le programme de résolution d'équation
[1] Second degré
[2] pass
[3] Quitter
"""
    )


if __name__ == "__main__":
    while True:
        try:
            menu()
            choice = int(input("Votre choix: "))
            if choice == 1:
                qe.runQE()
            elif choice == 2:
                menu()
                pass
            elif choice == 3:
                clear()
                print("Au revoir")
                break
            else:
                menu()
        except ValueError:
            menu()
