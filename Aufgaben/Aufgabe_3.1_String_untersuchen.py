"""
Aufgabe 3.1

Schreiben Sie ein Python-Programm, dass eine Zeichenkette von der Tastatur einliest und
dann die Anzahl der Großbuchstaben, Kleinbuchstaben und Ziffern in der Zeichenkette ausgibt.
Verwenden Sie zur Untersuchung der Zeichenkette die Funktion isupper(), islower() und isdigit().
"""

zk = input('Geben Sie eine Zeichenkette ein: \n')
upper = 0
lower = 0
digit = 0

for i in zk:
    if i.isupper():
        upper = upper + 1
    if i.islower():
        lower = lower + 1
    if i.isdigit():
        digit = digit + 1

print('Anzahl der Großbuchstaben:',upper)
print('Anzahl der Kleinbuchstaben:', lower)
print('Anzahl der Zahlen:', digit)

# Python Elegant
gb = sum(1 for c in zk if c.isupper())
print('Anzahl der Großbuchstaben:',gb)
kb = sum(1 for c in zk if c.islower())
print('Anzahl der Kleinbuchstaben:',kb)
d = sum(1 for c in zk if c.isdigit())
print('Anzahl der Zahlen:', d)