"""
Schreiben Sien ein einfaches "Schiffe versenken" Programm in Python.
Das Spielfelf ist 5 x 5 Felder groß.
Es soll ein Schiff an der Position (2,2) platziert werden.
Das Speilfeld soll bei jedem "Schuss" auf der Konsole als Tesxt ausgegeben werden.

a.) Der Benutzer kann nun die x-Koordinate und die y-Koordiniate eingeben.
Die Eingabe soll nun mit der Schiffsplatzierung verglichen werden.
Wenn das Schiff nicht getroffen urde, wird in die geratene Position der Spielfeldmatrix ein "*" geschrieben - beim Treffer ein "X".

b.) Bestimmen Sie für die Schiffsplatzierung einen zufälligen Wert
"""
# 2D Liste mit fünf einträgen
import random

spielfeldgroesse = 5

#Vorbereiten des Speilfels
s = [['O' for _ in range(spielfeldgroesse)]for _ in range (spielfeldgroesse)]

# zufällige Position des Schiffs
zeile0 = random.randint(1,spielfeldgroesse)
spalte0 = random.randint(1,spielfeldgroesse)

while True:
    # Spielfeld ausdrucken
    for i in range(spielfeldgroesse):
        for k in range(spielfeldgroesse):
            print(s[i][k],end="")
        print('')

    zeile = int(input('Zeile ='))
    spalte = int(input('Spalte ='))

    if zeile==zeile0 and spalte==spalte0:
        print('Schiff versenkt')
        break
    s[zeile-1][spalte - 1] = '*'