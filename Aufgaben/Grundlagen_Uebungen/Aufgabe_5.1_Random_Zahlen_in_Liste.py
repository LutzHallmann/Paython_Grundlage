"""
Aufgabe 5.1

Schreiben Sie ein Python Programm, welches 6 Zufallszahlen aus einem Intervall 1-49 erzeugt.
Diese 6 Zahlen sollen ausgegeben werden.
Diese 6 Zahlen sollen in einer Liste gespeichert werden.
Die Erzeugung der Zufallszahlen und die Ausgabe derer sollen jeweils in einer Funktion ausgelagert werden.
"""
import random
def ausgabe(a):
    print('Die Zahl lautet',str(a))
def zufallsInt(x):
   return random.randint(1,49)

lottozahlen = []
for i in range(1,6):
    i = zufallsInt(i)
    lottozahlen.append(i)
    ausgabe(i)
print(lottozahlen)