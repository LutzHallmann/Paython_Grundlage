"""
Schreiben Sie ein Python Programm, welche zwei Zufallszahlen zwischen 1 und 10 erzeigt.
Das Produkt dieser Zahlen soll in einer Variablen gespeichert werden.
Weiter kann der Benutzer eine Zahl eingeben, die dem Ergebnisse dieser Multiplikation entsprechen sollte,
ist diese eingegebene Zahl nicht gleich dem vom Rechner berechneten Zahl wird eine entsprechende Meldung ausgegeben.
Die Versuche werden gezählt
"""
import random
random.seed

zahl1 = random.randint(1,10)
zahl2 = random.randint(1,10)
versuch = 0
eingabe = -1
ergebnis = zahl1 * zahl2

while eingabe != ergebnis:
    versuch += 1
    eingabe = int(input(f'{zahl1} * {zahl2} = '))
    if eingabe != ergebnis:
        print('Das Ergebnis ist Falsch! Neuer Versuch!')
        continue
if versuch == 1:
    print(f'Sehr Gut! Sie brauchten {versuch} Versuch')
else:
    print(f'Sehr Gut! Sie brauchten {versuch} Versuche')
