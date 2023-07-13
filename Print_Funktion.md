# Print Funktion

Wenn wir Ausgaben tätigen möchten bedienen wir uns der print() Funktion.  
Die print() Funktion bietet verschiedene Möglichkeiten die Ausgabe zu gestalten, ins besondere die Parameter "sep" und "end".  
Die print() Funktion druckt beliebig vieler Werte aus.
Diese werden durch Kommata getrennt
```python
a = 3.456
print("a =", a)

>>> a = 3.456

# \n erzeugt einen Zeilenumbruch
print("a = \n", a)

# Seperator
print(34,56,23,23,56) # Ohne Seperator
print(34,56,23,23,56, sep=",") # mit Seperator als ","
>>> 34,56,23,23,56
print(34,56,23,23,56, sep=":-)") # mit Seperator als ":--)"
>>> 34:-)56:-)23:-)23:-)56

# in for-Schleife Daten Sammeln und am ende gesammelt ausgeben
for i in range(3):
    print(i,end=":-)")
>>> 1:-)2:-)3-)

# Umleitung in eine Datei
fh=open("daten.txt","w")
    print("Das ist eine Ausgabe", file=fh)
```

Die print() Funktion kennt verschiedene Parameter
1. **sep**  
    Dieser Parameter definiert eine Zeichenkette, die als "Trennzeichen" fungiert, welche die Ausgabe trennt.
2. **end**  
    Mit diesem Parameter kann ich den Zeilenabschluss definieren. Standardmäßig ist es ein Zeilenumbruch.  
    Ich kann diesen durch eine beliebige Zeichenkette ersetzen.  
    Möchte ich keinen Zeilenumbruch, so schreibt man: **end=""**
3. **file**  
    Mit diesem Parameter kann ich due Ausgaben in eine zuvor geöffnete Datei umlenken.  
4. Dazu wir dem Parameter der Datenkanal zugewiesen, auf dem die Ausgabe erfolgen soll.  
    
## Formatierte Stringliterale
Dabei geht es um das Formatieren von Strings ab Python 3.6.  
F-Strings bieten die Möglichkeit Ausdrücke mit einer minimalen Syntax zu formulieren.  
Es wird immer ein f vorangestellt.  
Die Ausdrücke werden in geschweiften Klammern notiert.  
Diese Ausdrücke werden zur Laufzeit ausgewertete.  
Die Ergebnisse werden dann durch die Ausdrücke in den geschweiften Klammern ersetzt.  
```python
name = "Fritz"
alter = 34
print(f"Der Name ist {name} und er ist {alter} Jahre alt!")
>>> Der Name ist Fritz und er ist 34 Jahre alt!

name2 = "Nils"
alter2= 27
#Berechnung mit String Literalen
print(f"{name} ist {abs(alter-alter2)} Jahre älter als {name2} alt")
>>> Fritz ist 7 Jahre älter als Nils 
```

```python
stadt = "Hamburg"
temperatur = 23.5
# Ausgabe formatieren in Float :6.2f
# Also ins Gesamt 6 Zeichen mit 2 Nachkommastellen
print(f"{stadt}: {(temperatur-32)*5/9:6.2f} Grad Fahrenheit") 
```
**Weiterführende Funktionen:**
 * Stringmodulo
 * format-Methode
```python
Bsp. Stringmodulo
print("Artikel: %5D, Preis %8.2f" %(453,65343))
```