from tkinter import messagebox
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from src import func as f


def runQE():
    root = tk.Tk()
    root.title("Équation du Second Degré")

    label_a = tk.Label(root, text="Valeur de A:")
    label_b = tk.Label(root, text="Valeur de B:")
    label_c = tk.Label(root, text="Valeur de C:")

    entry_a = tk.Entry(root)
    entry_b = tk.Entry(root)
    entry_c = tk.Entry(root)

    label_a.grid(row=0, column=0, padx=5, pady=5)
    label_b.grid(row=1, column=0, padx=5, pady=5)
    label_c.grid(row=2, column=0, padx=5, pady=5)
    entry_a.grid(row=0, column=1, padx=5, pady=5)
    entry_b.grid(row=1, column=1, padx=5, pady=5)
    entry_c.grid(row=2, column=1, padx=5, pady=5)

    def solve_second_degree():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            c = float(entry_c.get())
            result = deltaCalc(a, b, c)
            messagebox.showinfo("Résultat", result)

            if messagebox.askyesno("Graphique", "Afficher le graphique ?"):
                plot_trinome(a, b, c)

        except ValueError:
            messagebox.showerror(
                "Erreur", "Veuillez entrer des valeurs numériques valides."
            )

    solve_button = tk.Button(root, text="Résoudre", command=solve_second_degree)
    solve_button.grid(row=3, columnspan=2, pady=10)

    root.mainloop()

def plot_trinome(a, b, c):
    root = tk.Tk()
    root.title(f"Trinôme {a:.0f}x² + {b:.0f}x + {c:.0f}")

    fig, ax = plt.subplots()
    x = np.linspace(-10, 10, 100)
    y = trinome(a, b, c, x)
    ax.plot(x, y, label=f"{a:.0f}x² + {b:.0f}x + {c:.0f}")

    ax.axhline(0, color="r")
    ax.axvline(0, color="r")
    ax.set_xlabel("x : abscisse")
    ax.set_ylabel("f(x) : ordonnée")
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    root.mainloop()

def trinome(a, b, c, x):
    return a * x**2 + b * x + c


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
        return
