"""
Schreiben Sie ein Python-Programm,
welches mit Hifle der input()-Funktion zwei Zahlen von der Tastatur einliest
und die Quadrate dieser Zahlen auf der Python-Shell ausgibt.
"""

# Zahlen von der Tastatur einlesen
zahl1 = int(input("Bitte erste Zahl eingeben: "))
zahl2 = int(input("Bitte zweite Zahl eingeben: "))

print("Quadrat der Zahl", str(zahl1), "ist", str(zahl1 * zahl1))
print("Quadrat der Zahl", str(zahl2), "ist", str(zahl2 * zahl2))