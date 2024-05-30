import random
import tkinter as tk
from tkinter import messagebox


class Ricerca:
    def __init__(self):
        self.budgetRicerca = 0

        try:
            with open('ricerca.txt', 'r') as file:
                for linea in file:
                    chiave, valore = linea.strip().split(':')
                    valore = int(valore)
                    if chiave == 'budgetrimanente':
                        self.budgetRicerca = valore
                        print(f"{chiave}: {valore}")
        except FileNotFoundError:
            print("Errore: il file non è stato trovato.")

    def ricercaMateriale(self):
        stato_ricerca = random.randint(1, 4)
        resilienza=random.randint(0,250)
        duttilità=random.randint(0,150)
        costo = random.randint(1000000, 3000000)

        if self.budgetRicerca >= costo:
            self.budgetRicerca -= costo
            if stato_ricerca == 1:
                messagebox.showinfo("Risultato Ricerca", f"Materiale trovato! Budget rimanente: {self.budgetRicerca}\nCaratteristiche:\nResilienza:{resilienza}, Duttilità:{duttilità}")
                with open('storico.txt', 'a') as file:
                    file.write("Nuovo materiale trovato\n")
                    file.write("Caratteristiche\n")
                    file.write(f"Resilienza:{resilienza},Duttilità:{duttilità}\n")
                    file.write(f"Budget ricerca rimasto: {self.budgetRicerca}\n\n\n")
            else:
                messagebox.showinfo("Risultato Ricerca",
                                    f"Materiale non trovato, ma i fondi sono stati scalati. Budget rimanente: {self.budgetRicerca}")
                with open('storico.txt', 'a') as file:
                    file.write("Ricerca fallita, nessun materiale trovato\n")
                    file.write(f"Budget ricerca rimasto: {self.budgetRicerca}\n\n\n")
        else:
            messagebox.showwarning("Budget Insufficiente",
                                   f"Non ci sono abbastanza fondi per completare la ricerca. Budget rimanente: {self.budgetRicerca}")

        self.aggiornaBudgetRicerca(self.budgetRicerca)

    def avviaRicerca(self):
        self.ricercaMateriale()

    def aggiornaBudgetRicerca(self, nuovo_budget):
        self.budgetRicerca = nuovo_budget
        try:
            with open('ricerca.txt', 'w') as file:
                file.write(f"budgetrimanente:{self.budgetRicerca}")
            print("Aggiornamento budget riuscito")
        except Exception as e:
            print(f"Errore nell'aggiornamento del budget: {e}")


def main():
    ricerca = Ricerca()

    root = tk.Tk()
    root.title("Ricerca Materiale")

    budget_label = tk.Label(root, text=f"Budget Rimanente: {ricerca.budgetRicerca}")
    budget_label.pack()

    def aggiorna_label_budget():
        budget_label.config(text=f"Budget Rimanente: {ricerca.budgetRicerca}")

    def avvia_ricerca():
        ricerca.avviaRicerca()
        aggiorna_label_budget()

    ricerca_button = tk.Button(root, text="Avvia Ricerca", command=avvia_ricerca)
    ricerca_button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()