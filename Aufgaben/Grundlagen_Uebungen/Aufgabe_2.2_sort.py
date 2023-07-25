"""
Aufgabe 2.2

Schreiben Sie ein Python-Programm, welches drei Eingabe a,b,c (Ganzzahle) über die Konsole entgegennimmt
Hinweis: input()
Das Python-Programm soll nun die größe der eingegebenen Zahl bestimmen und ausgeben.
Verwenden Sie nicht die max() Funktion, sondern lösen Sie das Problem mit Hilfe von if-Verzweigungen.
"""

a = int(input("Geben Sie die erste Zahl ein: "))
b = int(input("Geben Sie die zweite Zahl ein: "))
c = int(input("Geben Sie die dritte Zahl ein: "))

maxZahl = c

if a >= b >= c:
    maxZahl = a
elif c < b:
    maxZahl = b

print("die größte Zahl ist:", str(maxZahl))

# Zweite Möglichkeit mit for Schleife
zahl = 0
for x in range(1,4):
    # Wir geben 3 Zahlen ein, nach jeder Eingabe
    # wird geprüft ob die eingegene Zahl groesser
    # wie die schon gespeicherte Zahl
    eingabe = int(input(fBitte {x}. Zahl eingeben:"))
    if eingabe > zahl:
        # wenn ja wird die neue eingegebene Zahl uebernommen
        zahl = eingabe
print("Die größte Zahl ist:", zahl)