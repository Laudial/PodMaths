import os
import math
import numpy as np
import matplotlib.pyplot as plt

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def runQE():
    clear()

    a = float(input("Valeur de A: "))
    b = float(input("Valeur de B: "))
    c = float(input("Valeur de C: "))

    clear()

    print(f"Equation : {a:.0f}x² + {b:.0f}x + {c:.0f}\n")
    print(deltaCalc(a, b, c))
    plot_trinome(a, b, c)


def trinome(a, b, c, x):
    return a * x**2 + b * x + c


def plot_trinome(a, b, c):
    # L'intervalle de trace
    x = np.linspace(-10, 10, 100)

    # La courbe
    plt.plot(x, trinome(a, b, c, x))

    # Les axes
    plt.axvline(x=0, color="r")
    plt.axhline(y=0, color="r")
    axes = plt.gca()
    axes.set_xlabel("x : abscisse")
    axes.set_ylabel("f(x) : ordonnée")

    plt.show()


def discriminant(a, b, c):
    return b**2 - 4 * a * c


def deltaCalc(a, b, c):
    delta = discriminant(a, b, c)
    if delta > 0:
        s1 = (-b - math.sqrt(delta)) / (2 * a)
        s2 = (-b + math.sqrt(delta)) / (2 * a)
        return f"Solution 1: {s1:.2f}\nSolution 2: {s2:.2f}"
    elif delta == 0:
        s0 = -b / (2 * a)
        return f"Solution : {s0:.2f}"
    else:
        return "Aucune solution"


if __name__ == "__main__":
    runQE()
