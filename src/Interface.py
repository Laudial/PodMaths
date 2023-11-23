import tkinter as tk
from tkinter import messagebox
from src import quadraticEquation as qe
from src import FDEquation as fde


def runIHM():
    root = tk.Tk()
    root.title("Résolution d'équations")

    def on_second_degree():
        second_degree_window = tk.Toplevel(root)
        second_degree_window.title("Équation du Second Degré")

        tk.Label(second_degree_window, text="Valeur de A:").grid(row=0, column=0)
        tk.Label(second_degree_window, text="Valeur de B:").grid(row=1, column=0)
        tk.Label(second_degree_window, text="Valeur de C:").grid(row=2, column=0)

        entry_a = tk.Entry(second_degree_window)
        entry_b = tk.Entry(second_degree_window)
        entry_c = tk.Entry(second_degree_window)

        entry_a.grid(row=0, column=1)
        entry_b.grid(row=1, column=1)
        entry_c.grid(row=2, column=1)

        def solve_second_degree():
            try:
                a = float(entry_a.get())
                b = float(entry_b.get())
                c = float(entry_c.get())
                result = qe.deltaCalc(a, b, c)
                messagebox.showinfo("Résultat", result)

                if messagebox.askyesno("Graphique", "Afficher le graphique ?"):
                    qe.plot_trinome(a, b, c)

            except ValueError:
                messagebox.showerror(
                    "Erreur", "Veuillez entrer des valeurs numériques valides."
                )

        tk.Button(
            second_degree_window, text="Résoudre", command=solve_second_degree
        ).grid(row=3, columnspan=2)

    def on_first_degree():
        first_degree_window = tk.Toplevel(root)
        first_degree_window.title("Équation du Premier Degré")

        tk.Label(first_degree_window, text="Coefficient de x:").grid(row=0, column=0)
        tk.Label(first_degree_window, text="Terme constant:").grid(row=1, column=0)

        entry_a = tk.Entry(first_degree_window)
        entry_b = tk.Entry(first_degree_window)

        entry_a.grid(row=0, column=1)
        entry_b.grid(row=1, column=1)

        def solve_first_degree():
            try:
                a = float(entry_a.get())
                b = float(entry_b.get())
                result = fde.equationFD(a, b)
                messagebox.showinfo("Résultat", result)

                if messagebox.askyesno("Graphique", "Afficher le graphique ?"):
                    fde.plot_equation(a, b)

            except ValueError:
                messagebox.showerror(
                    "Erreur", "Veuillez entrer des valeurs numériques valides."
                )

        tk.Button(
            first_degree_window, text="Résoudre", command=solve_first_degree
        ).grid(row=2, columnspan=2)

    tk.Button(root, text="Second degré", command=on_second_degree).pack()
    tk.Button(root, text="Premier degré", command=on_first_degree).pack()
    tk.Button(root, text="Quitter", command=root.destroy).pack()

    root.mainloop()


if __name__ == "__main__":
    runIHM()
