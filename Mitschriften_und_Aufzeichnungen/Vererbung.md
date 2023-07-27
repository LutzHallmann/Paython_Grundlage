# Vererbung
Klassen können vererbt werden.  
Dabei werden sämtliche Variablen und Methoden einer Klasse an sein Child vererbt.

Damit wir überhaupt Klassen erstellen können, ist in jeder Programmiersprachen eine "Basisklasse" implementiert
aus der sich alle Klasse, die wir erstellen, ableiten.

Ein Child kann nicht nur von einer Klasse Eigenschaften und Methoden erben... auch von mehreren.

Die Vererbung erfolgt wie hier beschrieben:
````python
class MyClass(str): # Wir erstellen ein Klasse und sagen, dass die Klasse alle Eigenschaften und Methoden der Klasse "str" erben soll.
    pass

class MyClass(str, int):    # Wir erben zuerst aus der Klasse "str" und dann aus der Klasse "int".
                            # Die Reihenfolge entscheidet, welche Variablen und Methoden überschrieben werden.

class MyOtherClass(MyClass):    # Erbt nun alles aus "str", "int" und "MyClass"
````

In Python ist die Abarbeitung der Elternklassen von links nach rechts!
````python
FrauenBehinderteParkplatz(Frauenparkplatz, Behindertenparkplatz):
# zuerst wird die Klasse Frauenparkplatz implementiert, danach Behindertenparkplatz
````

Wenn ich in meiner abgeleiteten Klasse einen Konstruktor verwende, werden die Konstruktoren der Elternklasse überschrieben.  
* Das bedeutet, dass die Elternklassen KEINE Instanzvariablen haben - also nur Klassenvariablen.  
Beim Aufruf einer Instanzmethode (also einer mit "self" als Parameter) erhalten wir die Fehlermeldung, dass wir zu wenig Parameter übergeben.
  * Lösung:  
    Aufruf des Elternkonstruktor in unserem eigenen Konstruktor:  
    super().__init__(self)
    -> super() durchsucht die Elternklasse(n) nach einem Konstruktor.  
    Auch hier von links nach rechts!!  
    Sobald ein Konstruktor gefunden wurde, wird dieser ausgeführt. Der erste Treffer zählt.  
    Wenn ich nun aus dem Beispiel (FrauenBehinderteParkplatz) BEIDE Elternteile benötige (Instanzvariablen),  
    dann müssen auch BEIDE instantiiert werden:
    * super() kenn zwei Parameter: super(Klassenname, Objekt)  
      Das übergebene Objekt wird dann dür den Aufruf in der instantiierung als "self" verwendet.
    * Frauenparkplatz.__init__(self) -> auch das funktioniert. So kann die Abarbeitung der Konstruktoren aufrufe selbst gesteuert werden.