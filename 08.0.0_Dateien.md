# Dateien
Dateien dienen dazu Daten in lokalen Dateiverzeichnis zu speichern.  
Dateien sollten , wenn man darauf zugreifen muss nicht zu groß werden. (Abgesehen von Protokolldateien)  
Die Datenmenge ist hierbei begrenzt, bei größeren Datenmengen sind Datenbanken die erste Wahl.  
Es gibt grundsätzlich zwei Verfahren, wie man Dateien handhaben kann.  
1. Sequenzieller Zugriff ohne feste Datensatzlänge
2. Wahlfreien Zugriff mit fester Datensatzlänge (Vorteil: Ich muss nicht alle Datensätze einlesen, wenn ich auf einen beliebigen Datensatz zugreifen möchte)

> zu 1.
> Für das Lesen von Daten benötigen wir die open() Funktion.  
> Mit dieser Funktion erzeugen wir ein Datenobjekt, welche eine Referenz auf dieses zurückgibt (Dateihandler).  
> Die  open() Funktion erwartet zwei Parameter.
> 1. Dateiname
> 2. Modus
>    * r = ausschließliches Lesen
>    * w = ausschließliches Schreiben - eine Datei mit gleichen Namen wird überschrieben
>    * a = ausschließliches Schreiben - existierende Datei wird nicht gelöscht, Daten werden angehängt

```python
# Allgemeine Syntax
open(filname, modus)
```
```python
Beispiel
fh = open('textdatei.txt', 'r')
```
## Lesen einer Datei
Üblicherweise list man eine Datei zeilenweise.  
Wenn eine Zeile eingelesen wird, sollte man das Zeilenende mit **rstrip()** bereinigen.  
(Also entfernt die Steuerzeichen am Zeilenenden z.B. \n oder \r)
```python
# Beispiel
fh = open('textdatei.txt', 'r')
for zeile in fh:
    print(zeile.rstrip())
fh.close()
```
## Schreiben in eine Datei
Zum Öffnen wird der w-Modus oder a-Modus gewählt.
```python
fh_in = open('textdatei.txt', 'r')
fh_out = open('textdatei_out.txt', 'w')

counter = 0     # Variable in der die Zeilen gezählt werden

for zeile in fh_in:
    counter += 1
    ausgabe = str(count) + ' ' + zeile.rstrip() + '\n' # Anlegen und befüllen der Ausgabe-Variable
    fh_out.write(ausgabe)   # Inhalt der Ausgabe-Variable in die Datei schreiben
    print(zeile.rstrip())

fh_in.close()
fh_out.close()
```
Mann kann auch die komplette Datei mit der Funktion readlines() einlesen
```python
dateiinhalt = open('textdatei.txt').readlines()
print(dateiinhalt)
```