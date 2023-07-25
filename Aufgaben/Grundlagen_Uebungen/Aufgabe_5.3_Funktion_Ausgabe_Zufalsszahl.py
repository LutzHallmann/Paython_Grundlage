"""
Aufgabe 5.3

Schreiben Sie eine Python Funktion mit dem namen "zufallszahl_in_bereich", die zwei Ganzzahlen als Argumente akzeptiert,
n und m, und eine zufällige Ganzzahl im Bereich von n bis m (einschließlich) zurückgibt
"""
import random

def zufallszahl_in_bereich(n,m):
    if isinstance(n, int) and isinstance(m, int):
        return random.randint(n,m)
    return 'Es wurden keine Integer Werte an die Funktion "zufallszahl_in_bereich" übergeben'


print(zufallszahl_in_bereich(1,10))