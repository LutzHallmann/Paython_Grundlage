
# Jede Variable, Funktion oder geladenes Modul,
# das hier geladen, definiert, initialisiert oder sonstiges wird,
# steht in der gesamten Klasse zur Verfügung

class Wuerfel():

    # Zuerst mal als Klassenvariablen
    INT_MinAugen = 1    # kleinste Augenzahl unseres Würfels
    INT_MaxAugen = 6    # höchste Augenzahl unseres Würfels
    
    #def __init__(self):
    def __init__(self, MinAugen: int, MaxAugen: int): # Wir erweitern um die Übergabe eines
                                    # Parameters mit der Absicht, dass dieser eine 
                                    # Ganzzahl sein soll
                                    # Man nennt das: Annotation
        # Wir erzeugen unsere Instanzvariablen und weisen diesen
        # unsere Werte der Klassenvariablen zu
        self.MinAugen = Wuerfel.INT_MinAugen
        #self.MaxAugen = Wuerfel.INT_MaxAugen
        try:
            self.MaxAugen = int(MaxAugen)
            self.MinAugen = int(MinAugen)
            if MaxAugen <= MinAugen:
                raise ValueError('MaxAugenzahl ist kleiner/gleich MinAugenzahl')
        except ValueError as err:
            return None
        '''
            Mit unserer Exception wird die Erzeugung des Objekts NICHT
            verhindert !!!!!!!!!!!!
            Wir können das Try-Except Konzept nur für die Steuerung unserer
            Programmabläufe innerhalb einer Methode nutzen.
        '''
    def wuerfeln(self):
        import random
        # Das Würfeln ist ja das erzeugen einer Zufallszahl
        # zwischen MinAugen und MaxAugen.
        # Wir benötigen das Modul "random"
        # randint(min, max) erzeugt eine Ganzzahl min und max jeweils inklusive
        return random.randint(self.MinAugen, self.MaxAugen)
    '''    
    def wuerfeln2():
        return Wuerfel.random.randint(INT_MinAugen, INT_MaxAugen)
    '''

''' Auskommentiert für "the next Step"
OBJ_MyWuerfel = Wuerfel()
print(OBJ_MyWuerfel.wuerfeln())
#print(Wuerfel.wuerfeln2())

# Naja .. welcher Vorteil hat das Ganze jetzt für mich?
# Das hätte man viiiiiiel kürzer als sequentielles Programm 
# (wie im Grundlagenkurs) schreiben können

# Wir können aus der Klasse soviele Objekte erzeugen, wie wir wollen.
# Jedes Objekt ist eigenständig
'''

'''
    Next Step:
    Wir haben unseren Konstruktor um einen Parameter ergänzt.
'''
OBJ_MyWuerfel = Wuerfel(5,3)
print(OBJ_MyWuerfel)
#print(OBJ_MyWuerfel.wuerfeln())
