'''
Der Umgang mit Daeteien ist eine Build-In Funktion
Allerdings, wenn es um die Arbeit mit Dateien (bsp.: Rechte) oder Verzeichnissen geht,
benötigen wir Module, die z.T. im Standard mit ausgeliefert werden. (z.B. pathlib)

In den Modulen haben wir Klassen, die wir instantiieren müssen.

Parameter für das Datei öffnen:
a       -> Append           ->  Datei wird im Schreibmodus geöffnet.
                                Der Dateizeiger wird aus das Enden de Datei gesetzt

w       -> Write            -> Datei wird geöffnet, wenn nicht vorhanden, wird diese Datei erzeugt,
                                wenn vorhanden, bleibt der Dateizeiger am Dateianfang.

a + w   -> Append + Write   -> Die Datei befindet sich im Exclusivmodus.
                                Für andere nur Lesezugriff auf diese Datei möglich

r       -> Read             ->  Datei wird im Lesemodus geöffnet.
                                Dateizeiger steht auf Anfang der Datei

a + r   -> Append + Read    ->  Ist eine Datei nicht vorhanden, wird ein Fehler ausgeworfen

t                           -> Der Inhalt der Datei wird als Text verarbeitet (Default).

b                           ->  Der Inhalt der Daten wird RAW verarbeitet. Keine Interpretation

t + b                       ->  zusätzliche Parameter zu a, w, r
'''

# Die Vorgehensweise ist immer dieselbe

try:
    dateihandler = open('textdatei.txt', 'wt')
        # Die Datei "textdatei.txt" wird im Text-Schreibmodus geöffnet, wenn nicht vorhanden wird diese erzeugt.

    dateihandler.write('Die Antwort auf alle Fragen ist: \42')
        # write arbeitet nicht ganz so wie print... es wird tatsächlich kein Zeichen hinzugefügt
    dateihandler.write('Per Anhalter durch die Galaxis \n')
    dateihandler.write('äöüß')
except PermissionError
    print('Hey ... dur hast keine Rechte')
except BaseException as err:
    print('Fehler:, err')
    exit()
else:
    dateihandler.close()    # Dateihandler wird geschlossen

# Auslesen unserer erstellten Datei:
dateihandler = open('textdatei.txt','rt')
for line in dateihandler:
    print(line, end='')    # print() setzt ja ein Zeilenende. Das haben wir aber
                        # schon in unserer Datei, damit wir Zeilen erkennen können
dateihandler.close()