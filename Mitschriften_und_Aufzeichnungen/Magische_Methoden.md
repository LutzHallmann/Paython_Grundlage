# Magische Methoden

Sind Methoden mit einer besonderen Bedeutung für Python und sind IMMER "private"
also mit 2 Underscores zu Beginn und 2 Underscores am Ende.  

Beispeil
```python
__init__(self): Konstruktor
__del__(self): Destruktor

a = b + c
```
Für Python sind ALLE Operatoren magische Methoden für die Klassen.  
In unserem Beispiel haben wir "=" (Wertzuweisung) und "+" als Operatoren

Vorgehensweise von links nach rechts:  
* Erezugung der Veariblen im Namenraum. Erzeugen des Dataobjekts (Datentypen ) indem Python versucht zu ermitteln,
welche Datenobjekte b und c sind um daraus das Datatobjekt für a zu bilden.  
Ins besondere speirl heir das Dataobjekt "None" eine Rolle.  
Kann Python im Moment nicht ermitteln, was für Dataobjekte a sein soll, wird ein None-Objekt erzeugt.  
* Jetzt schauen wir und den Operator "+" an:  
  * Python schaut im Objekt "b", ob es eine magische Methode "__add::" gibt.  
Wenn ja, wird diese Methode mit dem Paramter "c" aufgerufen.  
Es erfolgt also eine Objektübergabe.
  * Der Rückgabewert der Methode "__add__" wird dann Letzendlich entascheiden, welcher Datentyp "a" letztendlich haben wird.

**[Link Liste Magische Methoden]()**
