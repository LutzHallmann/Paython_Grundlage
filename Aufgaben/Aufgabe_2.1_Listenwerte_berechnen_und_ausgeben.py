"""
Aufgabe 2.1

Schreiben Sie für jede Zahlenreihe ein Python-Prgramm, welches folgende Zahlenreihen mit Hilfe von for-Schleifen auf einer Konsole ausgibt
Die Werte sollen berechnet und nicht einfach in einer Liste definiert werden!
"""

# a.) 4,5,6,7,8,9,10
zahlenreiheA = []
for i in range(4,11):
    zahlenreiheA.append(i)
print(zahlenreiheA)

# b.) 1,4,9,16,36,49,64
zahlenreiheB = []
for i in range(1,9):
    fib = i * i
    i = i + 1
    zahlenreiheB.append(fib)
zahlenreiheB.remove(25)
print(zahlenreiheB)

# c.) -1,1 , -2,2 , -4,4 , -5,5
zahlenreiheC = []
for i in range(0,-6, -1):
    k = float(i * 0.1 + i)
    zahlenreiheC.append(k)
zahlenreiheC.remove(-3.3)
print(zahlenreiheC)

# d.) 3,6,9,12,15,18,21
zahlenreiheD = []
for i in range(3,22,3):
    zahlenreiheD.append(i)
print(zahlenreiheD)
