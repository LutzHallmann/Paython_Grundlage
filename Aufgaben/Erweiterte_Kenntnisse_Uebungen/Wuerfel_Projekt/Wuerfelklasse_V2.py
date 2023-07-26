

class Wuerfel():

    # Zuerst mal als Klassenvariablen
    INT_MinAugen = 1    # kleinste Augenzahl unseres Würfels
    INT_MaxAugen = 6    # höchste Augenzahl unseres Würfels

    def __init__(self):
        self.MinAugen = 3
        self.MaxAugen = 5

    # Wir geben dem Objekt die Chance, seine Eigenschaften
    # zu verändern
    # Zuerst muss der Getter definiert werden "@property"
    @property
    def MinAugen(self):
        return self.MinAugen

    @MinAugen.setter
    def MinAugen(self, MinAugen: int):
        self.MinAugen = MinAugen

    @property
    def MaxAugen(self):
        return self.MaxAugen

    @MaxAugen.setter
    def MaxAugen(self, Param: int):
        self.MaxAugen = Param

    def wuerfeln(self):
        import random
        return random.randint(self.MinAugen, self.MaxAugen)


OBJ_MyWuerfel = Wuerfel()  # Erzeugung des Objekts ohne Parameter

# Wir nutzen nun die Getter und Setter Methoden
# Welche Methode angesteuert wird, wird über den Parameter entschieden:
# Ist ein Parameter vorhanden -> Setter
# Ist kein Parameter vorhanden -> Getter
OBJ_MyWuerfel.MinAugen(7)
OBJ_MyWuerfel.MaxAugen(12)
print(OBJ_MyWuerfel.wuerfeln())