# Grundstruktur eines Pythonprogramms

Grundsätzlich besteht ein Python Program aus einem Anweisungskopf und einem Anweisungskörper.
````python
Anweisungskopf:  
    Anweisung 1
    Anweisung 2
    ...
````
Prinzipiell können Quellcodezeilen beliebig lang sein.  
Wenn ich jedoch mit einer Zeile breite von ca. 80 Zeichen arbeiten möchte, kann mit der Backslash Notation "\" beliebig umbrechen.
```python
#z.B.
"Hallo Welt"

"Hallo" \
    "Welt"

# Es könne auch mehrere Anweisungen in einer Zeile stehen, diese müssen aber mit einem " ; " getrennt werden
print("Hallo"); print("Fritz")
```

## Kommentare
Kommentare werden in Python mit einem # eingeleitet. (Einzeilig)
Mehrzeilige Kommentare werden mit einem """ Mehrzeiliger Kommentar """
```python
# Einzeiliger Kommentar (Zeile mit # beginnen)

"""
Mehrzeiliger
Kommentar
(Eingefasst in 3 Anführungsstriche davor und danach)
"""
```

## Eingabefunktion
Um die Eingabe über die Tastatur entgegenzunehmen, verwenden wir die Input-Funktion
```python
name = input("Auszugebende Zeichenkette:")

# Eingabe reduzieren auf Integer
zahl = int(input("Auszugebende Zeichenkette:"))
```

## Kontrollstrukturen
Python Anweisungen sind normalerweise einzeilig.  
Sie werden nicht, wie in vielen anderen Programmiersprachen durch ein Semikolon geschlossen.  
Mehrzeilige Anweisungen sind erlaubt, wenn ihr Anfang und Ende durch eine Klammer eindeutig hergeht, wenn nicht, kann das mit einem Backslash kenntlich gemacht werden.  
Anweisungen dürfen mit einem Semikolon abgeschlossen werden.  
Werden mehrere Anweisungen in einer Zeile geschrieben werden diese durch ein Semikolon getrennt.  
```python
x = 5; y = 45; s = 4
```

### Blockelemente
In jeder Programmiersprachen gibt es Blöcke.  
Diese werden z.B. in Java durch geschweifte Klammern gekennzeichnet.
```java
if(Bedingung){
    Anweisungen des Block
    }
```
In Python gibt es ebenfalls Blöcke, diese werden mit einem Doppelpunkt eingeleitet ":"  
Alle weiteren Anweisungen müssen eingerückt werden.  
Die Klammern, wie in anderen Programmiersprachen entfallen!
```python
if Bedingung:
    Anweisung1
    ...
    Anweisung n
```
#### Richtig einrücken
Für das Ausmaß der Einrückung gibt es keine genauen Regeln. I.d.R reicht ein Zeichen,  
ich empfehle aber mehr als ein Zeichen,  
der Lesbarkeit wegen. → Wenn möglich keine Tabulatorzeichen verwenden.  
Es ist auch folgenden Variante möglich:
```python
if Bedingung:Anweisung
```
Mehrere Anweisungen:
```python
if Bedingung: Anweisung; Anweisung2; Anweisung3
```

In Python gibt es ebenfalls Blöcke, diese werden
Kontrollstrukturen ermöglichen es uns den linearen Ablauf eines Programms / Anweisungsfolgen zu durchbrechen.  
Es gibt zwei:
* Verzweigungen (Fallunterscheidungen)
* Schleifen (Wiederholungen)

> Verzweigungen ermöglichen es uns aufgrund einer Bedingung einen Codeblock auszuführen
> Es gibt zwei Arten von Verzweigungen:
> * if-Anweisung
> * Bedingte Ausdrücke
> Wir haben bei der if-Verzweigung einen Anweisungskopf und einen Codeblock (Anweisungskörper)   <br>
> 

Allgemeine Syntax:  
```python
if Bedingung:  
    Anweisung  
    Anweisung 2  
    ...  
    Anweisung n
``` 
**Beispiel:**
```python
x = 6

if x == 6:
    print("x hat den Wert 6")

if x == 6 or x > 13:
    print("x hat den Wert 6")
    print("oder x ist größer als 13")
```
Alternativen mit "else" in Python ist das "elif"

Allgemeine Syntax:
if Bedingung:  
    Anweisung 1  
        ...  
    Anweisung n  
elif Bedingung:  
    Anweisung 1  
        ...  
    Anweisung n  

**Beispiel:**
```python
x = 6
if x == 6:
    print("x hate den Wert 6")
elif x == 2:
    print("x hat den Wert 2")
# Zu einer If-Anweisung darf maximal ein else-Zweig gehören
else:   
    print("x hat weder den Wert 6 noch den Wert 2")
```

### Bedingter Ausdruck
**Beispiel**
```python
v = (20 if(x==1 else 30))
```
Damit ist es möglich den Wert einer Variablen oder allgemein die Zuweisung eines Wertes zu einer Variablen in Abhängigkeit einer Variablen gestalten

> A if Bedingung else B

Entweder nimmt man den Wert A an, wenn die Bedingung erfüllt ist, oder den Wert B wenn nicht.
Ich kann auch diese Bedingung nicht nur aus Zuweisung anwenden, sondern z.B. auch mit Ausgaben:

```python
x = 99
print("x hat de Wert 99" if x == 99 else "x ist ungleich 99")
```

## Schleifen
Für Schleifenkonstruktionen stehen uns die while-Schleife und die for-Schleife zur Verfügung.  
Die for-Schleife wird i.d.R. verwendet, wenn wir die Anzahl der Durchgänge kennen.  

### while-Schleife

**Allegemeine Syntax:** 
```python
         while Bedingung:
            Anweisung
                ...
            Anweisung n
```
Mit Hilfe der while Schleife kann ich eine Anweisungsfolge wiederholen.  
Diese Wiederholung erfolgt in Abhängigkeit der Bedingung(Schleifenbedingung)  
Der Schleifenkörper ist immer eingerückt.  
Die Wiederholung erfolgt so lange die Bedingung erfüllt ist.

**Beispiel**:
```python
zahl = 342
versuch = -1
zaehler = 0

while versuch != zahl:
    versuch = int(input("Bitte raten:"))
    
    if versuch < zahl:
        print("zu klein")
    if versuch > zahl:
        print("zu groß")

    zaehler = zaehler + 1
print("Sie haben in ",zaehler, "Versuchen geschafft")
```
** Beispiel 2**
Es solle eine einfachen while - Schleife programmiert werden, welchen die Zahlen von 1 bis 100 ausgibt:
```python
n = 100
# i ist eine Schleifenvariable
i = 1
while i <= n:
    print("Zahl:" + str(i))
    i = i + 1
```
Zeichenketten können nicht mit einem Integer-Wert erweitert werden.  
Es können immer nur zwei Zeichenketten miteinander verknüpft werden.  
Daher müssen wir Zahlenwerte immer mit er str() Funktion in einen String-Datentyp wandeln.

#### Break und Continue
Schleifen kann man mit diesen beiden Befehlen steuern.  
Mit **break** breche ich die Schleifen ab.  
Mit **continue** überspringe ich die Wiederholung (Iteration) und fahre mit der nächsten Wiederholung fort.

```python
n = 100
# i ist eine Schleifenvariable
i = 1
while i <= n:
    print("Zahl:" + str(i))
    # Wenn i ist gleich 50 dann breche die Schleife ab.
    if i == 50:
        break
    i = i + 1
```
```python
n = 100
# i ist eine Schleifenvariable
i = 1
while i <= n:
    i = i + 1
    print("Zahl:" + str(i))
    # Wenn i ist gleich 50 wird DIESER Schleifendurchlauf abgebrochen.
    # Alle weiteren Schleifendurchläufen werden ganz normal ausgeführt
    if i == 50:
        continue    
```
Üblicherweise verwendet man die break Anweisung im Zusammenhang mit der if-Anweisung.  
Bei der continue Anweisung wird der Schleifendurchlauf unterbrochen,  
dass alle nachfolgenden Anweisungen, die dem continue Befehl innerhalb der Schleife folgen, nicht ausgeführt werden.  
Der continue-Befehl sort also dafür, dass an den Anfang der Schleife gesprungen wird und die erste Anweisung der Schleife ausgeführt wird.  

### FOR-Schleife
Die for-Schleife wird i.d.R. verwendet, wenn die Anzahl der Wiederholungen bekannt ist.  
In Python besitzt diese Schleife die Funktion einer foreach-Schleife.  
Mit foreach-Schleife bezeichnet man eine Schleife, die ein Array iteriert.  
Das heißt es werden nacheinander alle Elemente dieser Liste ausgelesen.  
Um den Schleifenabbruch brauche ich mich nicht zu kümmern, denn dieser ist durch die Anzahl der Elemente dieser Liste / Array gegeben.  

```python
#Allgemeine Syntax:

for Variable in Sequenz:
    Anweisung1
    Anweisung2
    ...
    AnweisungN
```
**Beispiel**
```python
sprachen = ["C","C++","Java","Python"]

for sprache in sprachen:
    print(sprache)
```

Python kennt noch einen "else"-Block.  
Der else-Block wird ausgeführt, nachdem bei der for-Schleife alle Elemente durchlaufen wurden.  
Auch wenn die List, die durchlaufen werden soll leer ist, und der Schleifenblock gar nicht durchlaufen wurde.
```python
for Variable in Sequenz:
    Anweisung1
    Anweisung2
    ...
    AnweisungN
else:
    Anweisung3
```
**Beispiel**
```python
sprachen = ["C","C++","Java","Python"]

for sprache in sprachen:
    if sprache == "Python":
        print("Ich programmiere Python")
        break
    print(sprache)
else:
    print("Keine Programmierung")
print("Fertig")
```
