'''
Uebung 01
Werteliste(1:1,2:2,3:3....50:50)

- Bauen Sie die Werteliste
- sortieren Sie die Werteliste reverse
- geben Sie bitte nur alle ungeraden Werte aus der Werteliste aus
- erstellen Sie für jede der vorgenannten Aufgaben eine eigene Funktion
'''

# Definition und Initialisierung des Dictionarys
DIC_WerteListe = {}

# Teil 1 der Aufgabe: Erstellen der Werteliste
def erstellen(DIC_WerteListe):

    # Die Werteliste beginnt mit 1, deshalb der range beginnend mit 1
	for i in range(1, 51, 1):
		DIC_WerteListe[i] = i # Bei einem Dictionary müssen wir nicht mit append() arbeiten
	return DIC_WerteListe

# Teil 2 der Aufgabe: Reverse Sortieren
def sort_reverse(DIC_WerteListe):

	DIC_WerteListeReversed = {}
    # Wir benötigen sowohl den Key als auch den Wert
    # und durchlaufen die Liste entweder mit negativem Schrittwert
    # oder wir nutzen die Funktion "reversed"
	for key, value in reversed(DIC_WerteListe.items()):
		DIC_WerteListeReversed[key] = value
	return DIC_WerteListeReversed

# Teil 3 der Aufgabe: Ausgabe der ungeraden Werte
def ungeradeWerte(DIC_WerteListe):

    DIC_WerteListeUngerade = {}
    # Wie bei der Funktion "Sortieren" entweder mit Range
    # oder durch die Methode items()
    for key, value in DIC_WerteListe.items():
        if int(key) % 2 == 0: # Ist der Modulo ein Integer, ist der Wert gerade
            pass
        else    :  # Wir wollen nur ungerade Werte
            DIC_WerteListeUngerade[key] = value
    return DIC_WerteListeUngerade

print('Teil1:', erstellen(DIC_WerteListe), '\n')
print('Teil2:', sort_reverse(DIC_WerteListe), '\n')
print('Teil3:', ungeradeWerte(DIC_WerteListe), '\n')
