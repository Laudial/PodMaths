import numpy as np
import matplotlib.pyplot as plt
from src import func as f


def runEFD():
    f.clear()

    a = float(input("Coefficient de x : "))
    b = float(input("Terme constant : "))

    f.clear()

    print("\nEquation :", f"{a:.0f}x + {b:.0f} = 0\n")
    print(equationFD(a, b))

    graph = input("\nAfficher le graphique ? (O/N) ")
    if graph.lower() == "o":
        plot_equation(a, b)
    else:
        return None


def plot_equation(a, b):
    plt.figure("Equation du Premier Degré")

    # Le titre
    plt.title(f"Equation :{a:.0f}x + {b:.0f} = 0")

    # La courbe
    x = np.linspace(-10, 10, 100)
    y = a * x + b

    plt.plot(x, y, label=f"{a:.0f}x + {b:.0f}")

    # Les axes
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    axes = plt.gca()
    axes.set_xlabel("x : abscisse")
    axes.set_ylabel("y : ordonnée")

    plt.show()


def equationFD(a, b):
    if a == 0:
        if b == 0:
            return "L'équation a une infinité de solutions."
        else:
            return "L'équation n'a pas de solution."
    else:
        solution = -b / a
        return f"La solution de l'équation est : {solution:.2f}"


if __name__ == "__main__":
    runEFD()
