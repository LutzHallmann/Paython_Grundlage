"""
Aufgabe 3.2

Schreiben Sie ein Python-Programm, dass eine Zeichenkette vom Benutzer einliest un dann folgende Informationen ausgibt:
"""

zk = input('Geben Sie eine Zeichenkette ein: \n')

# 1.) Länge der Zeichenkette ausgeben
print('Länge der Zeichenkette ist:',len(zk))

# 2.) Das erste und das letzte Zeichen der Zeichenkette
print("Das erste Zeichen ist %s und der letzte Zeichen ist %s." % (zk[0], zk[-1]))

# 3.) Die Anzahl der Vokale in der Zeichenkette
zk_vokale_count = 0
for i in zk:
    if i in 'aeiouAEIOU':
        zk_vokale_count = zk_vokale_count + 1
print('Die Anzahl der Vokale ist:',zk_vokale_count)