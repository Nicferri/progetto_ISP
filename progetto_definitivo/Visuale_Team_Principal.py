import tkinter as tk
from tkinter import scrolledtext

class TeamPrincipal:


    def __init__(self):
        self.contenuto = ""
        self.leggiFile()
        self.crea_interfaccia()

    def leggiFile(self):
        try:
            with open('storico.txt', 'r') as file:
                self.contenuto = file.read()
        except Exception as e:
            self.contenuto = f"Errore: {e}"

    def crea_interfaccia(self):
        self.root = tk.Tk()
        self.root.title("Contenuto di storico.txt")


        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=40, height=20)
        self.text_area.pack(padx=10, pady=10)

        self.text_area.insert(tk.END, self.contenuto)

        self.root.mainloop()

def accediTeamPrincipal():
    TeamPrincipal()  # Crea un'istanza della classe TeamPrincipal

# Per avviare l'interfaccia grafica da un altro script, chiama la funzione accediTeamPrincipal
if __name__ == "__main__":
    accediTeamPrincipal()
