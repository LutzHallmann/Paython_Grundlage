# Strings
Für die Behandling von Zeichenketten gibt es viele Interessante Funktionen,  
einige möchten wir hier jetzt besprechen.  

## Aufspalten von Zeichenketten
Wenn wir einen String oder Daten einer Datei untersuchen möchten ist es sinnvoll diese aufzusplitten,  
um kleinere .. zu untersuchen.  
Python kenn hiefür die split() Funktion
```python
split()
# Diese Methode kann ohne Parameter aufgerufen werden:

zeichenkette = "Das ist ein Beispiel für eine Zeichenkette"
zeichenkette.split()
>>> ['Das','ist','ein','Beispiel','für','eine','Zeichenkette']
```

**Beispiel**
> **Datei mit dem namen: "adressen.txt"**
> 
> Meyer;Frank;Konstanz;93847583
> Walldinger;Tim;Memmingen;23738264
> Meiringer;Anna;Augsburg;3827496728
> 
> In einer Datei abgespeichert

### Daten aus einer Datei auslesen, in Tupel speichern sowie ausgeben
```python
fh = open("adressen.txt")
for adresse in fh:
    adresse = adresse.strip() # Whitespace entfernen
    (name,vorname,stadt,telefon) = adresse.split(';')
    print(vorname + " " + name + " ," + stadt + " ," + telefon)
fh.close()
```

```python
join()
# Diese Methode macht aus einer Liste wieder einen String

x = ['Apfel','Banane','Kirsche']
print(join(x))
```
### Suchen in Teilstrings
* Mit der Hilfe der Funktionen in "in" oder "not in" kannich prüfen, ob sich ein Suchstring in einer Zeichenkette befindet.
```python
zeichenkette = "Das ist ein Beispiel für eine Zeichenkette"

'Beispiel' in zeichenkette      # Zurückgegeben wird TRUE
'Beispiel' not in zeichenkette  # Zurückgegeben wird FALSE
```
* Hierbei gibt es keine Position zurüch, dafpür verwenden wir die Funktion find()
```python
zeichenkette = "Das ist ein Beispiel für eine Zeichenkette"

zeichenkette.find('Beispiel',15)    # >>> -1 (weil es dort nicht vorkommt)
```
* Zählen der Vorkommen eines Teilstrings mit count()
```python
zeichenkette = "Das ist ein Beispiel für eine Zeichenkette"

zeichenkette.count('Beispiel')  # >>> 1 (Weil es einmal vorkommt)
zeichenkette.count('in')        # >>> 2 (Weil es zweimal vorkommt
```
* Mit Hilfe der Funktion upper() und lower() kann ich die Zeichenkette in Gross oder Kleinbuchstaben wandeln.  
Die Prüfung erfolgt mit islower() und isupper()
```python
zeichenkette = "Das ist ein Beispiel für eine Zeichenkette"
e = zeichenkette.lower()    # >>> das ist ein beispiel für eine zeichenkette
e.zeichenkette.islower()    # >>> true

eu = zeichenkette.upper()   # >>> DAS IST EIN BEISPIEL FÜR EINE ZEICHENKETTE
eu.zeichenkette.isupper()   # >>> true
```