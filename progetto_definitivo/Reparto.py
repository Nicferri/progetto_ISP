import random
import tkinter as tk
from tkinter import messagebox
class Reparto:
    def __init__(self, dipendenti_totali=1000, budget_totale=150000000):
        self.dipendenti_totali = dipendenti_totali
        self.budget_totale = budget_totale


class Aerodinamica(Reparto):
    def __init__(self, nome="Aerodinamica", dipendenti_Anteriore=200, dipendenti_Posteriore=200, budget_Anteriore=30000000, budget_Posteriore=30000000):
       super().__init__()
       self.nome = nome
       self.dipendenti_Anteriore = dipendenti_Anteriore
       self.dipendenti_Posteriore = dipendenti_Posteriore
       self.budget_Anteriore = budget_Anteriore
       self.budget_Posteriore=budget_Posteriore

class PowerUnit(Reparto):
    def __init__(self, nome="Power Unit", dipendenti_MGUH=200, dipendenti_MGUK=200, budget_MGUK=30000000, budget_MGUH=30000000):
        super().__init__()
        self.nome = nome
        self.dipendenti_MGUH = dipendenti_MGUH
        self.dipendenti_MGUK = dipendenti_MGUK
        self.budget_MGUK = budget_MGUK
        self.budget_MGUH=budget_MGUH


class Ricerca(Reparto):
    def __init__(self,nome="Ricerca", dipendenti_Ricerca=200):
        super().__init__()
        self.nome=nome
        self.dipendenti_Ricerca=dipendenti_Ricerca

    budget_Ricerca=10000000
    def Ricerca_Materiale(self):
        global budget_Ricerca