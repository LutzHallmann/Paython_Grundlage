"""
Schreiben Sie ein Python Zahlenrateprgramm.
Es soll eine vom Rechner zufällig erzeugt ganze Zahl durch eine Benutzereingabe erraten werden.
Die Anzahl der Versuche soll gezählt und ausgeben werden
"""
import random

zahl = random.randint(1,1000)
versuch = -1
zaehler = 1

while versuch != zahl:
    versuch = int(input("Raten Sie: "))

    if versuch < zahl:
        print("zu klein")

    elif versuch > zahl:
        print("zu groß")

    if versuch == zahl:
        print("Super, Sie haben es in ", zaehler, "Versuchen geschafft")
        break

    zaehler += 1