import datetime
import random
from Reparto import PowerUnit
import tkinter as tk
from tkinter import messagebox


class MGUK(PowerUnit):
    def __init__(self, budget_MGUK, dipendenti_MGUK=50):
        super().__init__(dipendenti_MGUK=dipendenti_MGUK)
        self.budget_MGUK = budget_MGUK

    def creaMguk(self, costo, statoMGUK):
        if costo <= self.budget_MGUK:
            self.budget_MGUK -= costo
            return True, self.budget_MGUK
        else:
            return False, self.budget_MGUK


class MGUH(PowerUnit):
    def __init__(self, budget_MGUH, dipendenti_MGUH=50):
        super().__init__(dipendenti_MGUH=dipendenti_MGUH)
        self.budget_MGUH = budget_MGUH

    def creaMguh(self, costo, statoMGUH):
        if costo <= self.budget_MGUH:
            self.budget_MGUH -= costo
            return True, self.budget_MGUH
        else:
            return False, self.budget_MGUH


class PowerUnitGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestione PowerUnit")

        self.budgetMGUH = self.caricaBudgetDaFile('MGUH.txt')
        self.budgetMGUK = self.caricaBudgetDaFile('MGUK.txt')

        self.powerunit = PowerUnit()
        self.mguh = MGUH(budget_MGUH=self.budgetMGUH)
        self.mguk = MGUK(budget_MGUK=self.budgetMGUK)

        self.setup_gui()

    def caricaBudgetDaFile(self, filename):
        try:
            with open(filename, 'r') as file:
                for linea in file:
                    chiave, valore = linea.strip().split(':')
                    valore = int(valore)
                    if chiave == 'budgetrimanente':
                        return valore
        except FileNotFoundError:
            print(f"Errore: il file {filename} non è stato trovato.")
            return 0

    def setup_gui(self):
        tk.Label(self.master, text="Dipendenti MGUK:").grid(row=0, column=0, padx=10, pady=5)
        self.dipendenti_mguk_label = tk.Label(self.master, text=self.powerunit.dipendenti_MGUK)
        self.dipendenti_mguk_label.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.master, text="Dipendenti MGUH:").grid(row=1, column=0, padx=10, pady=5)
        self.dipendenti_mguh_label = tk.Label(self.master, text=self.powerunit.dipendenti_MGUH)
        self.dipendenti_mguh_label.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.master, text="Budget MGUK:").grid(row=2, column=0, padx=10, pady=5)
        self.budget_mguk_label = tk.Label(self.master, text=f"${self.mguk.budget_MGUK}")
        self.budget_mguk_label.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.master, text="Budget MGUH:").grid(row=3, column=0, padx=10, pady=5)
        self.budget_mguh_label = tk.Label(self.master, text=f"${self.mguh.budget_MGUH}")
        self.budget_mguh_label.grid(row=3, column=1, padx=10, pady=5)

        self.mguk_button = tk.Button(self.master, text="Crea MGUK", command=self.creaMguk)
        self.mguk_button.grid(row=4, column=0, padx=10, pady=10)

        self.mguh_button = tk.Button(self.master, text="Crea MGUH", command=self.creaMguh)
        self.mguh_button.grid(row=4, column=1, padx=10, pady=10)

    def creaMguk(self):
        costo = random.randint(1000000, 3000000)
        statoMGUK = random.randint(100, 200)
        success, budget_rimanente = self.mguk.creaMguk(costo, statoMGUK)
        if success:
            messagebox.showinfo("Successo", f"MGUK creata con successo! Costo: ${costo}, valore {statoMGUK}")
            self.save_to_file("MGUK.txt", costo, statoMGUK, budget_rimanente)

            now = datetime.datetime.now()
            formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")

            try:
                with open("storico.txt", "a") as file:
                    file.write(f"data produzione MGUK:{formatted_date_time}\n")
                    file.write(f"costoMGUK:{costo}\n")
                    file.write(f"valore MGUK:{statoMGUK}\n")
                    file.write(f"budget rimasto MGUK: {budget_rimanente}\n\n\n")
            except Exception:
                print ("errore nel file")


        else:
            messagebox.showerror("Errore", f"Fondi insufficienti per creare l'MGUK. Costo: ${costo}")
        self.update_budget_mguk_label(budget_rimanente)

    def creaMguh(self):
        costo = random.randint(1000000, 3000000)
        statoMGUH = random.randint(100, 200)
        success, budget_rimanente = self.mguh.creaMguh(costo, statoMGUH)
        if success:
            messagebox.showinfo("Successo", f"l'MGUH è creato con successo! Costo: ${costo}, valore {statoMGUH}")
            self.save_to_file("MGUH.txt", costo, statoMGUH, budget_rimanente)

            now = datetime.datetime.now()
            formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")

            try:
                with open("storico.txt", "a") as file:
                    file.write(f" data produzione MGUK:{formatted_date_time}\n")
                    file.write(f"costoMGUK:{costo}\n")
                    file.write(f"valore MGUK:{statoMGUH}\n")
                    file.write(f"budget rimasto MGUK: {budget_rimanente}\n\n\n")
            except Exception:
                print("errore nel file")

        else:
            messagebox.showerror("Errore", f"Fondi insufficienti per creare l'MGUH. Costo: ${costo}")
        self.update_budget_mguh_label(budget_rimanente)

    def save_to_file(self, filename, costo, stato, budget_rimanente):
        try:
            with open(filename, "w") as file:
                file.write(f"costo:{costo}\n")
                file.write(f"stato:{stato}\n")
                file.write(f"budgetrimanente:{budget_rimanente}\n")
        except Exception as e:
            print(f"Errore durante il salvataggio del file: {e}")

    def update_budget_mguk_label(self, budget_rimanente):
        self.budget_mguk_label.config(text=f"${budget_rimanente}")

    def update_budget_mguh_label(self, budget_rimanente):
        self.budget_mguh_label.config(text=f"${budget_rimanente}")


def accedi_powerunit():
    root = tk.Tk()
    app = PowerUnitGUI(master=root)
    root.mainloop()


if __name__ == "__main__":
    accedi_powerunit()