"""
Aufgabe 5.6

Erstellen Sie eine Funktion namens "concat_strings, die eine beliebige Anzahl von Strings akzeptiert und all diese Strings zu einem einzigen String (concatenates).
Wenn keine Strings übergeben werden, sollte die Funktion einen leeren String zurückgeben.
"""
def concat_strings(*n):
    Ausgabe=""
    for x in n:
        Ausgabe+= x
    return Ausgabe

print(concat_strings("Dies", " ist"," ein"," Text."))