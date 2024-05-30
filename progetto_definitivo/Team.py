import tkinter as tk
from tkinter import messagebox

dati_file = [
    ('MGUH.txt', "budgetrimanente:30000000\n"),
    ('MGUK.txt', "budgetrimanente:30000000\n"),
    ('telaio_post.txt', "budgetrimanente:30000000\n"),
    ('Anteriore.txt', "budgetrimanente:30000000\naliDisp:0\n"),
    ('ricerca.txt', "budgetrimanente:30000000\n")
]


for nomeFile, data in dati_file:
    try:
        with open(nomeFile, 'w') as file:
            file.write(data)
    except FileNotFoundError:
        print(f"Errore: il file {nomeFile} non è stato trovato.")

    try:
        with open("storico.txt", 'w') as file:
            file.write("")
    except FileNotFoundError:
        print ("error")


class Team:

    global dipendenti_totale
    dipendenti_totale = 1000
    global budget_tot
    budget_tot = 150000000
    def __init__(self, root):
        self.aerodinamica_completata = False
        self.powerunit_completata = False
        self.root = root
        self.root.title("login team")
        self.root.geometry("250x200")
        self.creaWidget()

    def creaWidget(self):
        tk.Label(self.root, text="nome utente:").grid(row=0, column=1, padx=10, pady=5)
        tk.Label(self.root, text="password:").grid(row=4, column=1, padx=10, pady=5)

        self.username_entry = tk.Entry(self.root)
        self.password_entry = tk.Entry(self.root)

        self.username_entry.grid(row=1, column=1, padx=10, pady=5)
        self.password_entry.grid(row=5, column=1, padx=10, pady=5)


        login_button = tk.Button(self.root, text="accedi", command=self.login)
        login_button.grid(row=7, column=1, padx=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "gara" and password == "gara":
            if self.aerodinamica_completata and self.powerunit_completata:
                import gara
                gara
            else:
                messagebox.showerror("errore", "Non hai completato la macchina, completala e riprova")

        elif username == "powerunit" and password == "powerunit":
            self.powerunit_completata = True
            import powerunit
            powerunit.accedi_powerunit()

        elif username == "aerodinamica" and password == "aerodinamica":
            self.aerodinamica_completata = True
            import Aerodinamica
            Aerodinamica.accedi_aerodinamica()

        elif username == "teamprincipal" and password =="teamprincipal":
            import Visuale_Team_Principal
            Visuale_Team_Principal.accediTeamPrincipal()

        elif username == "ricerca" and password == "ricerca":
            import ricerca
            ricerca.main()




if __name__ == "__main__":
    root = tk.Tk()
    team = Team(root)
    root.mainloop()
