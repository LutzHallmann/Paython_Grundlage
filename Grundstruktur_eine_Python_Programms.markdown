# Grundstruktur eines Python Programms

Grundsätzlich besteht ein Python Program aus einen Anweisungskopf und einem Anweisungskörper.
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
Um die Eingabe über die Tastatur entgegenzunehmen, verwenden wir die Inputfunktion
```python
name = input("Auszugebende Zeichenkette:")

# Eingabe reduzieren auf Integer
zahl = int(input("Auszugebende Zeichenkette:"))
```

## Kontrollstrukturen
Kontrollstrukturen ermöglichen es uns den linearen Ablauf eines Programms / Anweisungsfolgen zu durchbrechen.  
Es gibt zwei:
* Verzweigungen (Fallunterscheidungen)
* Schleifen (Widerholungen)

> Verzweigungen ermöglichen es uns aufgrund einer Bedingung einen Codeblock auszuführen
> Es gibt zwei Arten von Verzweigungen:
> * if-Anweisung
> * Bedingte Ausdrücke
> Wir haben bei der if-Verzweigung einen Anweisungskopf und einen Codeblock (Anweisungskörper)   <br>
> 
> Allgemeine Syntax:  
> if Bedingung:  
    Anweisung  
    Anweisung 2  
    ...  
    Anweisung n

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

Entweder nimmt man den Wert A an, wenn die Bedinung erfüllt ist, oder den Wert B wenn nicht.
Ich kann auch diese Bedingung nicht nur aus Zuweisung anwenden sondernz.B. auch mit Ausgaben:

```python
x = 99
print("x hat de Wert 99" if x == 99 else "x ist ungleich 99")
```

## Schleifen
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