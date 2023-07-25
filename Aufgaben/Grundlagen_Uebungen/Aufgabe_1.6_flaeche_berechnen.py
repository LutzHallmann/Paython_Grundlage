"""
Aufgabe 1.6

Schreiben Sie ein Python-Programm, welches mit Hilfe input()-Funktion zwei Zahlen von der Tastatur einliest.
Diese zwei Zahlen repräsentieren die Länge und Breite eines Rechtecks.
Geben Sie den Flächeninhalt für diese beiden eingegebenen Werte eines Rechtecks aus.

a.) Geben Sie eine negative Nachricht auf der Shell aus, sobald negative Werte eingegeben worden sind.
"""

print("Flächenberechnung für ein Rechteck!")
laenge = float(input("Bitte Länge eingeben: "))
while laenge < 0:
    print("Es muss eine positive Zahl eingeben werden")
    laenge = float(input("Bitte Länge eingeben: "))

breite = float(input("Bitte Breite eingeben: "))
while breite < 0:
    print("Es muss eine positive Zahl eingeben werden")
    breite = float(input("Bitte Breite eingeben: "))

print("Der Flächeninhalt beträgt", str(laenge * breite))
