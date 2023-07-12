"""
Aufgabe 3.3

Schreiben Sie ein Python-Programm, dass eine Zufallszahl zwischen 1 und 6 erzeugt.
Der Benutzer soll nun in einer while-Schleife die Möglichkeit haben, die Zahl zu raten.
Die Anzahl der Rateverusche soll gezählt und ausgegeben werden.
Arbeiten Sie mit der randint() Funktion aus dem random-Modul, welches Sie mit "import" einbinden.
"""
import random
random.seed

zahl = random.randint(1,6)
versuch = -1
zaehler = 1

while versuch != zahl:
    print(str(zaehler) + '.', 'Versuch')
    versuch = int(input('Raten Sie: '))
    if versuch == zahl:
        print('Super Sie haben die Zahl', zahl, 'in', zaehler, ' Versuchen richtig erraten')
        break
    zaehler += 1

