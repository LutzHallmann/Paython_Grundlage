"""
Aufgabe 2.4

Schreiben Sie ein Python-Programm, welches mit Hilfe der input()-Funktion drei Zahlen von der Tastatur einliest und dann deren Durchschnitt auf der Konsole ausgibt.
"""

a = int(input("Geben Sie die erste Zahl ein: "))
b = int(input("Geben Sie die zweite Zahl ein: "))
c = int(input("Geben Sie die dritte Zahl ein: "))

print("Der Durchschnitt ist:", str((a + b + c) / 3))

# Zweite Möglichkeit mir for Schleife
zahl = 0
for x in range(1,4):
    eingabe = int(input(f"Bitte {x}. Zahl eingeben:"))
    zahl = (zahl*(x-1)+eingabe)/x
print("Die größte Zahl ist:", zahl)