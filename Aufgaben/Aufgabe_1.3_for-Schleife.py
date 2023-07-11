"""
Aufgabe 1.3

Schreiben Sie ein Python-Programm, welches die Zahlen zwischen 1 und 250 mit Hilfe einer for-Schleife auf der Pyton-Shell ausgibt.
a.) Der Bereich zwischen 100 und 150 soll nicht ausgegeben werden.
b.) Es sollen nur alle geraden Zahlen ausgegeben werden.
c.) Es sollen die Zahlen und die Quadrate dieser Zahlen jeweils nebeneinander ausgegeben werden.
"""

# for-Schleife, die Zahlen zwischen 1 und 250 ausgibt
# Range(start, stop, step)
for i in range(0,251,2):
   # a.) Der Bereich zwischen 100 und 150 soll nicht ausgegeben werden.
   if 100 < i < 150:
       continue
   print(str(i), "Quadrat=", str(i*i))