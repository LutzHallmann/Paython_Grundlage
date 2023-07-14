# Generatoren und Iteratoren
## Iteratoren
Iteratoren haben wir in for-Schleifen kennengelernt.  
Iteratoren durchlaufen die Elemente einer Liste.  
```python
staedte = ['Hamburg','Paris','Berlin']
for stadt in staedte:
    print('Stadt: ' + stadt)

# Ausgabe:
# Stadt: Hamburg
# Stadt: Paris
# Stadt: Berlin
```
> Bevor die for-Schleife gestartet wird, ruft Python die eingebaute Funktion "iter" mit der Liste staedte als Argument auf.  
> Die Funktion "iter" liefert ein Objekt zurück, mit dem es möglich ist die Elemente der Liste zu durchlaufen.  
> Das heißt der Rückgabewert von iter(staedte) ist ein Element der Klasse "ier_iterator".  
> Nach jedem Schleifendurchlauf wird die next() Funktion mit der nächstfolgenden Zeiger position aufgerufen.  
> Das geht so lange weiter, bis der Iterator am Ende der Liste angelangt ist.
```python
#Beispiel 1
staedte = ['Hamburg','Paris','Berlin']
zeiger = iter(staedte)
print(next(zeiger))
print(next(zeiger))
print(next(zeiger))
# Hamburg
# Paris
# Berlin

# Beim 4. Aufruf kommt ein Fehler, da wir nun außerhalb des Index sind
```
```python
# Beispiel 2
staedte = ['Hamburg','Paris','Berlin']
zeiger = iter(staedte)
while True
    try:
        stadt = next(zeiger)
    except StopIteration:
        break
    print('Stadt: ' + stadt)
```
##