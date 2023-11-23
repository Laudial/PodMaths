from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk


def runEFD():
    root = tk.Tk()
    root.title("Équation du Premier Degré")

    label_a = tk.Label(root, text="Coefficient de x:")
    label_b = tk.Label(root, text="Terme constant:")

    entry_a = tk.Entry(root)
    entry_b = tk.Entry(root)

    label_a.grid(row=0, column=0, padx=5, pady=5)
    label_b.grid(row=1, column=0, padx=5, pady=5)
    entry_a.grid(row=0, column=1, padx=5, pady=5)
    entry_b.grid(row=1, column=1, padx=5, pady=5)

    def solve_first_degree():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            result = equationFD(a, b)
            messagebox.showinfo("Résultat", result)

            if messagebox.askyesno("Graphique", "Afficher le graphique ?"):
                plot_equation(a, b)

        except ValueError:
            messagebox.showerror(
                "Erreur", "Veuillez entrer des valeurs numériques valides."
            )

    solve_button = tk.Button(root, text="Résoudre", command=solve_first_degree)
    solve_button.grid(row=2, columnspan=2, pady=10)

    root.mainloop()


def plot_equation(a, b):
    root = tk.Tk()
    root.title("Graphique de l'Équation du Premier Degré")

    fig, ax = plt.subplots()
    x = np.linspace(-10, 10, 100)
    y = a * x + b
    ax.plot(x, y, label=f"{a:.0f}x + {b:.0f}")

    ax.axhline(0, color="black", linewidth=0.5)
    ax.axvline(0, color="black", linewidth=0.5)
    ax.set_xlabel("x : abscisse")
    ax.set_ylabel("y : ordonnée")
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    root.mainloop()


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
