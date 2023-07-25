"""
Erstellen Si in Python eine Liste von fünf Städtenamen.
Danach füge Sie zwei weitere Städte an das Ende der Liste hinzu.
Geben Sie am Ende die aktualisierte Liste und die Länge der Liste auf der Konsole aus.
"""

staedte = ['Hamburg','Hannover','Berlin','München','Köln']
print(staedte)
staedte.extend(['Kiel','Flensburg'])
print(staedte)
staedte.pop(2)
print(staedte)