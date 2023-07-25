"""
Aufgabe 3.6

Schreiben Sie ein Python Programm, dass eine Zeichenkette vom Benutzer einliest und die Anzahl der Wörter in der Zeichenkette ausgibt.
Verwenden Sie dafür die split() Funktion
"""
zk = input('Bitte eine Zeichenkette eingeben: \n')
zk = zk.split()
for i in zk:
    if i.isdigit():
       zk.remove(i)
print('Es sind', len(zk),'Wörter in der Zeichenkette enthalten')