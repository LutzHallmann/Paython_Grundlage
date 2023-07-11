
# Operatoren

Operatoren dienen dazu Ausdrücke oder Literale miteinander zu verknüpfen.
Wir unterscheiden zwischen verschieden Gruppen von Operatoren:

## Arithmetischen Operatoren

| Operator| Ergebnis |
|---------|---|
|+ Addition|Summe von z.B. x und y|
|- Subtraktion|Differenz aus x und y|
|/ Division|Quotient von x und y|
|% Restwertdivision (Modulo)<br/>Wir immer genutzt um zu prüfen ob eine Zahl teilbar ist.|Rest beim Teilen von x und y 15%4=3|
|** Potenz |x hoch y z.B. x**y|
|// Ganzzahliger Quotient|Abgerundeter Quotient von x und Y, x//y|
                       

## Vergleichende Operatoren

| Operator |Ergebnis|
|----------|---|
| ==       |a == b wahr, wenn a und b gleich sind|
| !=       |ungleich|
| <        |kleiner als|
| <=       |kleiner gleich|
| \>       |größer als|
| \>=      |größer gleich|
> Vergleichende Operatoren benötigen wir immer dann, wenn wir Ausdrücke für Bedingungen und damit Verzweigungen formulieren möchten.  
Diese können auch ergänzt werden mit Hilfe von logischen Operatoren.  
Denn damit ist es möglich Ausdrücke miteinander zu verknüpfen
> ```python
> a > 7 and a < 3
> ```



| Operator | Ergebnis                                                                          |
|----------|-----------------------------------------------------------------------------------|
| not      | ist die Umkehrung des Ausdrucks (nicht)                                           | 
| and      | und: ist wahr wenn beide Teilausdrücke wahr sind                                  |
| or       | oder: ist wahr wenn der eine oder der andere Teilausdruck war ist, nicht exklusiv |

not:
Ein "true" Wert wird hiermit zu "false":z.B. not a < 4

and:
a < 9 and d > 10

or:
a > 6 or a > 12

## Spezielle Operatoren
Python verfügt über eine Reih von spezielle Operatoren

> "in" Operator

Mit Hilfe dieses Operator kann man prüfen, ob sich ein bestimmtes Element in einer Liste befindet

```python
liste = ["eins", "3.0", "vier"]
"3.0" in liste

>>> True
``` 

## Verkettungsoperator
> "+ und +="

```python
name = "Meier"
vorname = "Franz"
namegesamt = vorname + " " + name
```
```python
b = "Musik"
v = "veranstaltung"
b += v

>>> "Musikveranstaltung"
```

## Wiederholung von Sequenzen
```python
* und *=
```

```python
3 * "xyz"

>>> xyzxyzxyz
```
```python
mann = "Hallo"
mann *= 3

>>> "HalloHalloHallo"
```
```python
zeichenfolge = "abcdefg"
zeichenfolge[4]
>>> 'e' #Es wird mit Null angefangen zu zählen
```

| Index vorne  | 0  | 1  | 2  | 3  | 4  | 5  |
|--------------|----|----|----|----|----|----|
| Elemente     | a  | b  | c  | d  | e  | f  |
| Index hinten | -6 | -5 | -4 | -3 | -2 | -1 |

### Teilsequenz:
```python
# Zwischen einen bestimmten Indexbereich
zeichenfolge = "abcdefg"
zeichenfolge[2:5]

# Ab einen bestimmten Index
zeichenfolge[:5]

# Bis zu einem bestimmten Indexpunkt
zeichenfolge[5:]

# Zwischen einen bestimmten Index Bereich in zweier schritte
zeichenfolge[1:4:2]
```