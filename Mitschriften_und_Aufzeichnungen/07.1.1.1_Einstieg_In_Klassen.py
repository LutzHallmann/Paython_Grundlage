class MyClass():    #Definition einer Klasse
    INT_MyVar1 = 50     # Klassenvariablen -> stehen ohne Instanzen zur Verfügung
    INT_MyVar2: int    # Klassenvariablen mit Typ -> nur Informativ
    STR_MyVar3: str = '... und Danke für den Fisch'

    # Klassenvariablen sind innerhalb der Klasse als "globale" Variablen verfügbar.
    # Dazu stehen Klassenvariablen auch von außerhalb zur Verfügung

print(MyClass.STR_MyVar3)   # Zugriff auf eine Klassenvariable

dir(MyClass)    # Listet auf was alles in "MyClass zur Verfügung steht

# Konstruktor
def __init__(self, STR_SomeData, STR_OtherData) # self ist IMMER der erste Parameter für eine Methode
                                                # self Repräsentiert ALLE Instanzvariablen (In Java ist es "this")
    self.data = STR_SomeData        # Instanzvariablen
    self.other = STR_OtherData      # Instanzvariablen
    STR_SomeListe = [1,2,3]         # lokale Methodenvariablen

    # Hinweis an Programmierer, dass die Variablen "Geschützt" sein sollen
    self._divident = 5  # 1 x Underscore -> restricted
    self.__divisor = 1  # 2 x Underscore -> private
                        # Bei 2 x Underscore macht es uns Python etwas schwerer auf die Variabel zuzugreifen.
                        # Die Variable wir in den Namensraum con "self" mit dem Klassennamen vorangestellt aufgenommen.
                        # Angesprochen: Objektname._Klassenname__Variablenname

# Destruktor
def __del__(self):      # Der Destruktor wird automatisch aufgerufen
    print('Objekt wurde zerstört')

print(MyClass.STR_MyVar3)   # Zugriff auf eine Klassenvariable
# Wir haben getestet, ob der Destruktor auch bei der Beendigung aufgerufen wird,
# ohne das wie ein Objekt instantiiert haben.
OBJ_MyObj = MyClass(3,5)    # Instantiiere der Klasse MyClass -> wir erzeugen ein Objekt
# Auch hier wird bei Programmende der Destruktor nicht aufgerufen
del OBJ_MyObj
# Jetzt hat der Modul-Garbage Collector zugeschlagen und den Destruktor aufgerufen
OBJ_MyObj = MyClass(3,5)
print(OBJ_MyObj.data)
OBJ_MyObj2 = MyClass(5,10)
print(OBJ_MyObj2.data)

# Wir lassen uns die die Werte der Klassenvariablen ausgeben - sind natürlich identisch
print(OBJ_MyObj.INT_MyVar1, OBJ_MyObj2.INT_MyVar1)

# Wir verändern den Wert der Klassenvariablen
MyClass.INT_MyVar1 = 100
print(OBJ_MyObj.INT_MyVar1, OBJ_MyObj2.INT_MyVar1)
# Bei beiden Objekten wurde die entsprechende Klassenvariable geändert.

MyClass.STR_MyVar4 = 'Per Anhalter durch die Galaxis'
print(OBJ_MyObj.STR_MyVar4) # Es wurde von außerhalb einer Klasse eine neue Klassenvariable definiert und ihr einen Wert zugewiesen.
                            # Automatisch steht nun die Klassenvariable ALLEN Objekten zur Verfügung.
                            # Gewünscht, wenn wir bei neuronalen Netzen Erfahrungen an alle Knoten des Netzes weitergeben wollen
                            # Absolut NICHT gewünscht bei unserer herkömmlichen Programmierung.

# Verändern von Instanzvariablen
OBJ_MyObj.data = 20
print(OBJ_MyObj.data)

# Ist natürlich gefährlich... genauso wie folgendes
OBJ_MyObj.new = 3   # Neue Instanzvariable für das Objekt
print(OBJ_MyObj.new)
# Bei Schreibfehlern für Variablennamen... ob nun Klasse oder Instanz, erhalten wir KEINE Fehlermeldung bei einer Wertezuweisung.
# Es wird einfach eine neue Variable angelegt.

# In anderen Programmiersprachen kennen wir den Schutz von Variablen und Methoden durch die Schlüsselwörter "privat", "restricted" usw.
# In Python ist das NICHT möglich.
# Wir können die Absicht des Programmierers, dass eine Variable oder Methode Private oder Restricted sein soll durch Underscore darstellen.
# Dazu wurden Änderungen an der Klasse MyClass durchgeführt.

# Wir haben die Änderung durchgeführt und die private Variablen __divisor erstellt sowie die restricted Variable _divident
print(OBJ_MyObj._divident)
print(OBJ_MyObj._MyClass__divisor)

# Was passiert hier:
# INT_MyVar1 ist ja eine Klassenvariable, die in jede, Objekt verfügbar ist.
OBJ_MyObj.INT_MyVar1 = 25
# Es wird nicht die Klassenvariable angesprochen, sondern es wird eine neue Instanzvariable angelegt.