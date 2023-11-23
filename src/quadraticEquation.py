import math
import numpy as np
import matplotlib.pyplot as plt
from src import func as f


def runQE():
    f.clear()

    a = float(input("Valeur de A: "))
    b = float(input("Valeur de B: "))
    c = float(input("Valeur de C: "))

    f.clear()

    print(f"Equation : {a:.0f}x² + {b:.0f}x + {c:.0f}\n")
    print(deltaCalc(a, b, c))

    graph = input("\nAfficher le graphique ? (O/N)")
    if graph.lower() == "o":
        plot_trinome(a, b, c)
    else:
        return None

def trinome(a, b, c, x):
    return a * x**2 + b * x + c

def plot_trinome(a, b, c):
    plt.figure(f"Trinôme {a:.0f}x² + {b:.0f}x + {c:.0f}")

    # Le titre
    plt.title(f"f(x) = {a:.0f}x² + {b:.0f}x + {c:.0f}")

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
