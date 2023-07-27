class Parkplatz():
    INT_Breite = 200
    INT_Hoehe = 240
    INT_Laenge = 300
    HEX_Farbe = '#ffffff'
    BOL_Aktiv = True
    BOL_Besetzt = False

    # Konstruktor
    def __init__(self):
        self.__breite = Parkplatz.INT_Breite
        self.__hoehe = Parkplatz.INT_Hoehe
        self.__laenge = Parkplatz.INT_Laenge
        self.__farbe = Parkplatz.HEX_Farbe
        self.__aktiv = Parkplatz.BOL_Aktiv
        self.__besetzt = Parkplatz.BOL_Besetzt


    @property
    def Breite(self):
        return self.__breite

    @Breite.setter
    def Breite(self, breite):
        if breite < Parkplatz.INT_Breite:
            pass
        else:
            self.__breite = breite


    @property
    def Laenge(self):
        return self.__laenge

    @Laenge.setter
    def Laenge(self, laenge: int):
        if laenge < Parkplatz.INT_Laenge:
            pass
        else:
            self.__laenge = laenge

    @property
    def Hoehe(self):
        return self.__hoehe

    @Hoehe.setter
    def Hoehe(self, hoehe: int):
        if hoehe < Parkplatz.INT_Hoehe:
            pass
        else:
            self.__hoehe = hoehe

    @property
    def Farbe(self):
        return self.__farbe

    @Farbe.setter
    def Farbe(self, farbe: str):
        self.__farbe = farbe

    @property
    def Aktiv(self):
        return self.__aktiv
    @Aktiv.setter
    def Aktiv(self, aktiv: bool):
        self.__aktiv = aktiv

    @property
    def Besetzt(self):
        return self.__besetzt
    @Besetzt.setter
    def Besetzt(self, besetzt: bool):
        self.__besetzt = besetzt

    def __str__(self):
        return '%s\n Breite: %d \n Länge: %d \n Höhe: %d  \n Farbe: %s' \
            % (self.__class__.__name__, self.__breite, self.__laenge, self.__hoehe, self.__farbe)

    def __del__(self):
        print('Das Objekt wurde gelöscht')

