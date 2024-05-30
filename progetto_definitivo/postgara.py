import tkinter as tk
from tkinter import messagebox
def visualizzaStatoMacchina (self):
    try:
        with open("stato_macchina.txt", "r") as file:
            contenuto = file.read()
            self.log_text.delete(1.0, tk.END)
            self.log_text.insert(tk.END, "\n--- Stato della Macchina ---\n")
            self.log_text.insert(tk.END, contenuto + "\n")
    except FileNotFoundError:
        messagebox.showerror("Errore", "Il file stato_macchina.txt non esiste.")

    self.log_text.insert(tk.END, "se si vuole procedere con la creazione di nuovi componenti premere accedi reparti\n")
    self.log_text.insert(tk.END, "altrimenti creare una nuova simulazione\n")
