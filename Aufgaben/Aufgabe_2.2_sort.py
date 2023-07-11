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

if a > b > c:
    maxZahl = a
elif c < b:
    maxZahl = b

print("die größte Zahl ist:", str(maxZahl))
