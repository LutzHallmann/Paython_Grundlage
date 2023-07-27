########################
# Chunkübertragung
########################

'''
    Zugriff auf eine entfernte Datei mit HTTP
'''
import urllib.request as ur  # Bibliothek für das Arbeiten mit reinen HTTP-Übertragungen
import sys

url = 'http://www.business-rules.org/files/2023KW16Python.zip'
chunksize = 64 * 1024  # 64 KByte .. die Chunksize muss in Bytes angegeben werden
filename = 'D:\KITPython.zip'  # Name und Verzeichnis der lokalen Datei

dateihandler = ur.urlopen(url)  # Wir öffnen die externe Datei
laenge = dateihandler.length  # Größe der Datei in Bytes
print(laenge)

counter = 0

with open(filename, 'wb') as f:
    while True:  # Aufbau einer Endlosschleife
        chunk = dateihandler.read(chunksize)  # wir holen 64KB vom Server
        if not chunk:  # erhalten wir keine Daten, brechen wir die Schleife abs
            break
        f.write(chunk)
        counter += chunksize
        # Feedback für die Ausgabe
        # print('+') # Ausgabe eines Plus-Zeichens für jede 64KiB
        if int((counter / laenge) * 100) % 10 == 0:
            print('+', end='', flush=True)
            '''
            sys.stdout.flush() # stdout -> Standardausgabe (Windows = Kommandofenster)
                                # flush() zwingt den Zeichenbuffer, sich zu entleeren
            '''
    print()

dateihandler.close()