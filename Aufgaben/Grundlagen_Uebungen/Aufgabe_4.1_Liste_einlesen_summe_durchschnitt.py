"""
Aufgabe 4.1

Schreiben Sie ein Python-Programm,
dass eine Liste von Zahlen einliest und dann die Summe und den Durchschnitt dieser Zahlen ausgibt.
Wenn die Liste leer ist, soll das Programm eine entsprechende Meldung ausgegeben werden.
"""
# Zahlenlisten automatisch mit Zufallszahlen generieren und in der Datei "Aufgabe_4.1_Zahlenlisten.txt schreiben
import random
datei = open('Aufgabe_4.1_Zahlenliste.txt', 'w')
for i in range(1,1000,1):
    i += 1
    datei.write(str(random.randint(1,10000))+';')
datei.close()

# Die oben erstellte generierte Liste einlesen
datei = open('Aufgabe_4.1_Zahlenliste.txt', 'r')
zahlenliste = []
zahlenlisteInt =[]
for zahlenListe in datei:
    zahlenListe = zahlenListe.split(';')
    if zahlenListe.index(''):
        zahlenListe.remove('')
    for i in zahlenListe:
        if i.isdigit():
            zahlenListeInt = zahlenlisteInt.append(int(i))
        else:zahlenListeInt = zahlenlisteInt.remove(i)
print(zahlenlisteInt)
anzahl = len(zahlenlisteInt)
print('Anzahl der Einträge:',anzahl)
durchschnitt = (sum(zahlenlisteInt)) / anzahl
print('Berechneter Durchschnitt:',durchschnitt)