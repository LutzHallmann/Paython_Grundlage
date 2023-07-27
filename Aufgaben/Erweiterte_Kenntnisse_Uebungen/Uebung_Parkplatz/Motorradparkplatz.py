# Definieren der Klasse Motorradparkplatz
import Parkplatz

class Motorradparkplatz(Parkplatz):
    INT_Breite = 150    # Die hier definierte Klassenvariable überschreibt die Klassenvariable aus Parkplatz
    INT_Laenge = 200
    BOL_Motorrad = True

    def __init__(self):
        # Wir haben festgestellt, dass durch eine eigene __init__ Probleme auftreten beim Zugriff aus "self"
        # Wir haben ein EIGENES "self"
        super().__init__()  # Aufruf der Elternklasse
        self.breite = Motorradparkplatz.INT_Breite
        self.laenge = Motorradparkplatz.INT_Laenge


OBJ_MyMotorrad = Motorradparkplatz()
