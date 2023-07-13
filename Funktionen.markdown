# Funktionen (eigene Funktionen definieren)
Funktionen haben den Zweck grundsätzlich Redundanz (Wiederholungen) zu vermeiden.  
Redundanz ist immer unbequem, wenn es darum geht eine zuverlässige Wartbarkeit des Programms zu ermöglichen.  
Allgemein kann man sagen, sobald ich ein Programmteil, mehr als einmal benötige formuliere ich daraus eine Funktion.  
Des Weiteren kann es sein, dass ich die Funktionen zur Erhöhung der Übersichtlichkeit definiere.  
Die Allgemeine Form der Funktionsdefinition in Python lautet:
```python
def funktionsname(parameter1,parameter2,...,parameterN):
    code
```
### Es gelten folgende Regeln:  
1. Funktionen müssen definiert werden, bevor diese aufgerufen werden.
2. Funktionen ohne Parameter sind möglich. Die runden Klammern dürfen jedoch NIE vergessen werden.
3. Funktionen könne vorzeitig verlassen werden. Dafür verwende man das Schlüsselwort "return"
4. Mit dem Schlüsselwort "return" kann ich werte zurückgeben. Das Schlüsselwort ist option.
5. Ich kann immer nur einen Wert zurückgeben. Über den Umweg Listen, Tupel usw. kann ich mehrere Werte in ein Listenobjekt verpacken.
6. Funktionen dürfen schachtelt werden. Das kommt in der Praxis recht selten vor. da diese dann auch nur in dieser Funktion verwendet werden kann.
   (Thema des fortgeschrittenen Kurses)
7. Es ist nicht erlaubt, dass mehrere Funktionen den gleichen Namen haben.

### Wir unterscheiden 4 verschiedene Typen von Funktionen
1. Funktionen ohne Übergabe und Rückgabewert.
2. Funktionen mit Übergaben und ohne Rückgabewert
3. Funktionen ohne Übergabe und mit Rückgabewert
4. Funktionen mit Übergabe und mit Rückgabewert
```python
#Funktionsdefinition
def ausgabe():
        print('Hallo Funktion')

# Aufruf der Funktion
ausgabe()

def f1(x,y):
    print('Parameter 1:',x)
    print('Parameter 2:',y)

#Aufruf von f1
f1(2,3)
>>> 'Parameter 1: 2'
>>> 'Parameter 2: 3'

def quadrat(x):
    return x * x

quadrat_ergebnis = quadrat(3)
print(quadrat_ergebnis)
>>> 9
```
### Variable Anzahl von Parametern
Üblicherweise ist die Anzahl der Parameter einer Funktion bekannt.  
Es kann aber auch Anwendungsfälle geben, die mit einer unbekannten Anzahl an Parameter einer Funktion arbeiten müssen.  
Zur Definition von Parametern wird der "*" Operator verwendet.
```python
# Beispiel

def orte(stadt,*andereOrte):
    print(stadt,andereOrte)

orte('Berlin')

orte('Berlin','Freiburg','Paris')
```

### Lokale und Globale Variablen

#### Folgendes Beispiel (global): 
```python
def f1():
    print(x)
x = 3
f1() # Ausgabe
```
> Funktionen können Variablen lesen, die außerhalb der Funktion definiert sind.
Wenn Variablen innerhalb einer Funktion definiert sind und initialisiert werde, sind diese lokal
Grundsätzlich solle man am besten lokale Variablen verwenden, weil dadurch sichergestellt ist, dass die geforderten Vorgaben. bzg. der Wertigkeit erfüllt werden.
Bei globalen Variablen kann der aktuelle Wert schwer kontrollieren. Ins Besondere bei großen Programmen.

#### Folgendes Beispiel (lokal):
```python
def f1():
    y = 6
    print(y)
f1() # Ausgabe
print(y) # Fehlermeldung

# Aufpassen, wenn globale und lokale Variablen die gleiche Bezeichnung haben
def f1():
    y = 6
    print(y)
y = 9
f1() # es wird die 6 ausgegeben
print(y) # es wird die 9 ausgegeben
# Diese zweifach definierten Variable, sind völlig unabhängig voneinander.
```

#### Optionale Parameter
Innerhalb der Signatur einer Funktion kann eine Parameterliste definiert werden.  
Dabei ist es möglich für jeden Parameter einen Standardwert zu definieren.  
Der Standardwert kommt immer dann zum Tragen, wenn der Parameter nicht übergeben wird.
```python
def f(a,b,c= -1,d=0):
    print(a,b,c,d)
f(6,7,8,4)      # Ausgabe 6 7 8 4
f(6,7,8)        # Ausgabe 6 7 8 0
f(a=6,b=6,d=9)  # Ausgabe 6 7 -1 9
f(6)            # Fehler weil b fehlt
f(b=6,c=9)      # Fehler weil a fehlt
```