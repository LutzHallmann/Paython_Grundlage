"""
Aufgabe 5.2

Schreiben Sie eine Python Funktion namens ist_bischof, die eine Ganzzahl n als Argument akzeptiert und überprüft,
ob diese Zahl eine Bischofszahl ist oder nicht.
Eine Bischofszahl ist eine natürliche Zahl, deren Quersumme 2 ist.
Wenn die Zahl eine Bischofszahl ist, soll die Funktion True zurückgeben, ansonsten False.

Zum Beispiel ist 1100 eine Bischofszahl, weil die Quersumme der Ziffer 1+1+0+0=2 ist.
"""
def ist_bischof(x=0):
    if isinstance(x,int):
        ergebnis = 0
        while x:
            ergebnis += x % 10
            x = int(x / 10)
        if ergebnis == 2:
            return True
    else:
        return 'Es handelt nicht um ein Ganzzahl, welche an die Funktion "ist_bischof" übergeben wurde'

print(ist_bischof(1100))