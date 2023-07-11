"""
Aufgabe 2.4

Schreiben Sie ein Python-Programm, welches mit Hilfe der input()-Funktion drei Zahlen von der Tastatur einliest und dann deren Durchschnitt auf der Konsole ausgibt.
"""

a = int(input("Geben Sie die erste Zahl ein: "))
b = int(input("Geben Sie die zweite Zahl ein: "))
c = int(input("Geben Sie die dritte Zahl ein: "))

durchschnitt = (a + b + c) / 3

print("Der Durchschnitt ist:", str(durchschnitt))