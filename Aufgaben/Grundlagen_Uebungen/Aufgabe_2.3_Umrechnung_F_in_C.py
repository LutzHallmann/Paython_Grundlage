"""
Aufgabe 2.3

Schreiben Sie ein Python-Program, welches Fahrenheit nach Celsius umrechnet.
Es soll die Möglichkeit gegeben sein, einen Fließkommawert eingeben zu können input() Dieser ist der Fahrenheitwert

Schreiben Sie nun ein Programm, welches die Umrechnung in Celsuis vornimmt.

Formel: celsius = 5*(fahr-32)/9
"""

fahr = float(input("Geben Sie die Temperatur in Fahrenheit ein: "))

print("es sind umgerechnet ", 5*(fahr-32)/9, "Grad Cellsius")
