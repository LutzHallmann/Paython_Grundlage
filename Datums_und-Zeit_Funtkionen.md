# Datums und Zeit Funktionen
Für die Zeitfunktionen benötigen wir das **time-Modul**.  
Dort ist alles vorhanden, was man zum Umgang mit der Zeit braucht
```python
import time

# Zeit in Sekunden
print('Zeit in Sekunden:',time.time())

# Ausgabe: Zeit in Sekunden: 1689324808.0370054

# aktuelle Lokale Zeit
print('Aktuelle Zeit',time.localtime())
# Ausgabe: Aktuelle Zeit time.struct_time(tm_year=2023, tm_mon=7, tm_mday=14, tm_hour=10, tm_min=57, tm_sec=43, tm_wday=4, tm_yday=195, tm_isdst=1)
# Die Ausgabe ist ein Tupel
lokaleZeit = time.localtime()

# Tupel auspacken
jahr, monat, tag = lokaleZeit[0:3]
print(f'Datum:{tag:02d}.{monat:02d}.{jahr:02d}')
# Ausgabe: Datum:14.07.2023

# Mit der strftime() Funktion hat man die Möglichkeit den Zeitstring detailliert zu bearbeiten
print(time.strftime('Tag.Monat.Jar:%d.%m.%Y',lokaleZeit))   # Für weitere Formatierungen gibt es eine gesonderte Code Tabelle
# Ausgabe: Tag.Monat.Jar:14.07.2023
```