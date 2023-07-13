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
1. Funktionen iohne Übergabe und Rückgabewert.
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