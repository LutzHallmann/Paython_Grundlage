def allesFinden(heuhaufen,nadel,pos=0):
    pos = heuhaufen.find(nadel,pos)
    while pos != -1: # Solange sucht, wie Stellen gefunden werden.
            pos=heuhaufen.find(nadel,pos+1) # erneute Such mit einem Offset. Als ab der nächsten Stelle wo es gefunden wurde.
            yield pos
text="Das ist ein Beispieltext mit einer Funktion damit man eine Stelle wiederfindet"

positionen = allesFinden(text, 'ein')
print(positionen,type(positionen))

for index,position in enumerate(positionen):
    print(f'{index+1:d}. Position : {position:d}')

