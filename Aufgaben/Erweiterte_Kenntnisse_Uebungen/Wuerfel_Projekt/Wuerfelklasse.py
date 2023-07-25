'''
Wir legen den Grundstein für unseren Würfen.

Eigenschaften des Würfels:
- Zu Beginn begnügen wir uns mit einem Würfel der die Augenzahlen 1- 6- würfen kann

Methoden:
- naja... einfach mal würfeln
'''

# Jede Variable, Funktion oder geladene Modul,
# das heir geladen, definiert, initialisiert oder sonstiges,steht in der gesamten Klasse zur Verfügung
import random

class Wuerfel():

    # Zuerst mal als Klassenvariablen
    INT_MinAugen = 1    # kleinste Augenzahl unseres Würfels
    INT_MaxAugen = 6    # höchste Augenzahl des Würfels

    """
    def __init__(self):
        # Wir erzeugen unsere Instanzvariablen un weisen diesen unsere Werte der Klassenvariable zu.
        '''
        self.MinAugen = INT_MinAugen
        self.MaxAugen = INT_MaxAugen
        '''
        # Bei der Erzeugung des Objekts geht der Zugriff nur über den Klassennamen
        self.MinAugen = Wuerfel.INT_MinAugen
        self.MaxAugen = Wuerfel.INT_MaxAugen
    """
    def __init__(self, Param: int):             # Wir erweitern um die Übergabe eines Parameter mit der Absicht,
                                                # dass dieser eine Ganzzahl sein soll.
                                                # Man nennt das "Annotation"
        # Wir erzeugen unsere Instanzvariablen und weisen diesen unsere Werte der Klassenvariablen zu
        self.MinAugen = Wuerfel.INT_MinAugen
        try:
            self.MaxAugen = int(Param)
        except:
            return False

    def wuerfeln(self):
        # Das Würfeln ist ja das erzeugen einer Zufallszahl
        # zwischen MinAugen und MaxAugen.
        # Wir benötigen das Modul "random"
        # randint (min, max) erzeugt eine Ganzzahl min und max jeweils inklusive
        return random.randint(self.MinAugen, self.MaxAugen)

# Beim erzeigen des Objekts erhalten wir auf einmal eine Fehlermeldung,
# dass INT_MinAugen im Konstruktor nicht definiert ist.
'''
Erklärung:
Wenn wir aus der Klasse ein Objekt erzeugen, könne wir auf die Klassenvariablen nur noch über den Klassennamen zugreifen!
'''
# OBJ_MyWuerfel = Wuerfel()
# print(OBJ_MyWuerfel.wuerfeln())

# Aus der Klasse können so viele Objekte erzeugt werden wie man will.
# Jedes Objekt ist eigenständig

'''
Next Step:
Wir haben unseren Konstruktor um einen Parameter ergänzt
'''
OBJ_MyWuerfel = Wuerfel(5)
print(OBJ_MyWuerfel.wuerfeln())

