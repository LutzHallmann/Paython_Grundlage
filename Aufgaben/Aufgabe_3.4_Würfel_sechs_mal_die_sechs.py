"""
Aufgabe 3.4

Schreiben Sie ein Python Programm, welches einen Würfel simuliert.
Das Programm soll solange laufe, bis 6 mal die Sechs "gewürfelt wurde.
Die Anzahl der Versuche ist auszugeben
"""
import random
random.seed

zahl = None
zaehler = 1
sechsen = 0

while sechsen < 6:
    zahl = random.randint(1, 6)
    if zahl == 6:
        sechsen += 1
    zaehler += 1
print('Es brauchte:', zaehler, 'Versuche')
