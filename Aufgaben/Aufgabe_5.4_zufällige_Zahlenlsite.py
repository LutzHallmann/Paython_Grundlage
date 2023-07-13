"""
Aufgabe 5.4

Schreiben Sie eine Python Funktion namens "zufaellige_zahlen_liste", die zwei Argument akzeptiert:
Anzahl und Bereich

a.) Die Funktion soll eine Liste mit Anzahl zufälliger Ganzzahlen generieren, die alle im Bereich von 0 bis bereich liegen (einschließlich).
Die generierten Zahlen dürfen in der Liste wiederholt werden.
"""
import random

def zufaellige_zahlen_liste(anzahl=0,bereich=0):
    if isinstance(anzahl, int) and isinstance(bereich, int):
        zahlenliste = []
        for i in range(0,anzahl,1):
            zahlenliste.append(random.randint(0,bereich))
        return zahlenliste
    return 'Es wurden keine Integer Werte an die Funktion "zufallszahl_in_bereich" übergeben'


print(zufaellige_zahlen_liste(50,10))
