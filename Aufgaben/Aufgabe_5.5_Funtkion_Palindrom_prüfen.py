"""
Aufgabe 5.5

Schreiben Sie eine Python Funktion mit dem Namen "ist_palindrom", die einen String als Argument akzeptiert und überprüft, ob dieser String ein Palindrom ist.
Ein Palindrom ist ein Wort, dass von vorne und hinten gleich gelesen wird, z.B. "radar" oder "anna".
Die Funktion soll True zurückgeben, wenn der String ein Palindrom ist, und False, wenn er kein Palindrom ist.
"""
def  ist_palindrom(n=""):
    Liste1=[x.lower() for x in n]
    Liste2= [x.lower() for x in n]
    Liste2.reverse()
    if Liste1==Liste2: return True
    else: return False

print("ist_palindrom('Anna') :",ist_palindrom("Anna"))
print("ist_palindrom('Jonn') :",ist_palindrom("Jonn"))