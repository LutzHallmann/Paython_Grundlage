import  sqlite3 as sql
import sys, os

# Das Modul os stellt uns Mittel zur Verfügung, mit dem Betriebssystem zu kommunizieren.
# Unter anderen z.B. Betriebssystembefehle absetzen

try:
    if os.path.exists('firma.db'):
        pass
    else:
        raise BaseException
    connection = sql.connect('firma.db')    # in sqLite die Datei, die als Datenbank angesprochen werden soll.
                                            # Ist die Date nicht vorhanden, wird diese erzeugt.
    cursor = connection.cursor()    # Ein Cursor für unsere SQL-Statement

except BaseException as err:
    print('Eine Verbindung konnte nicht hergestellt werden', err)
    sys.exit()  # Sysexit kann ein ein aufgerufenen Programm Informationen in der Form von Integer-Werten von 0-9 zurückliefern

sql = 'select * from person'    # Zeige alle Spalten und alle Datenzeilen aus der Tabelle Personen an

cursor.execute(sql) # Das SQL-Statement wird nun im bereitgestellten Cursor ausgeführt
                    # Nach der Ausführung des SQLite (und jedes andere DBMS)
                    # Das Ergebnis im Cursor da.
                    # Diesen Können wir nun durchlaufen
                    # 2. Möglichkeit:
                    # - wir holen uns den Datensatz für Datensatz
for dsatz in cursor:    # Fir liefert uns ein Tupel der Datenfelder zurück.
                        # Dazu wird intern die Methode: fechone() verwendet, die wir auch manuell aufrugfen könnten über cursor.fetchone
    print(dsatz[0], dsatz[1])   # Zugriff auf die Datenfelder über den Indes des Tuper

# 2. Möglichkeit: Wir lassen uns das Ergebnis mit fetchall übergeben
# Bei fetchall erhalten wir eine 2-dimensionale Liste:
# 1te Dimension = Datensätze 2te Dimension = Spalten (als Tupel)
gesamtdaten = cursor.fetchall() # Die 2-dimensionale Liste

connection.close()
