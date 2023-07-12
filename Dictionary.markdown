# Dictionarys
**Dictionarys sind veränderbar!**  
Hier können wir Zuordnungen von Schlüsseln und Werte speichern (Key-Value-Paaren)
Key-Value Paar werden durch ":" getrennt.  
Die Liste wird in geschweifte Klammer geschrieben.  
z.B. d={"k1":"w1","k2":"w2"}

> Dictionary -> dict  

Ein Dictionary enthält beliebig viele Schlüssel-Werte Parrw (key-value pairs).  
Der Schlüssel muss nicht unbedingt eine Zahl sein.
```python
woerterbuch = {'Germany':'Deutschland','Sweden':'Schwede'}

#andere Variante
woerterbuch = {0:1,
               'Sweden':'Schweden',
               'abc':0.5}

woerterbuch = {[1,2,3]:"abc",
               'Sweden':'Schweden',
               'abc':0.5}
```
Bei einem Dictionary handelt es sich um einen **ungeordneten** Datentyp.  
Das bedeutet das der Schlüssel nicht zwingend in der Reihenfolge durchlaufen wird, in der dem Dictionary hinzugefügt wurde.  

Der Zugriff auf einen Wert erfolgt immer über den Schlüssel.
```python
>>>woerterbuch['Germany']
'Deutschland'

# Verändern des Eintrags:
>>> woerterbuch['Germany'] = 'Bayern'

# Löschen eines Schlüssel -Werte-Paares
del woerterbuch['Germany']

#Prüfen ob ein bestimmeter Schlüssel vorhanden ist:
>>> 'France' in woerterbuch
False

# Zwei Dictionarys kann man auch kombinieren:
# Mit Hilfe des Pipe "|"
{'Germany':'Deutschland','Sweden':'Schweden'} | {'France':'Frankreich','Poland':'Polen'}

d = {}
d = | {'Germany':'Deutschland','Sweden':'Schweden'}
d = | {'France':'Frankreich','Poland':'Polen'}

#kombinieren der beiden Dictionarys
d = {}
d = | {'Germany':'Deutschland','Sweden':'Schweden'}
e = | {'France':'Frankreich','Poland':'Polen'}
n = d | e
```

## Schlüssel definieren (Key Value Paare)
```python
d={"Schlüssel":"wert1", "Schlüssel2":"Wert2"}
print(d)
```
## einen Schlüssel ausgeben
```python
d["Schlüssel"]
print(d["Schlüssel"]) 
# In der Eckigen Klammer wird der Schlüssel angegeben. Ausgegeben wird der Wert zum Schlüssel
```

## Funtkionen
```python
d = {}
d = | {'Germany':'Deutschland','Sweden':'Schweden'}
d = | {'France':'Frankreich','Poland':'Polen'}

# Löscht das Dictionary d
d.clear()

# Liefert ein iterierbares Objekt, dass alle Schlüssel - Werte Paare von d
d.items()
d = {'k1':'v1','k2':'v2','k3':'v3','k4':'v4'}
for paar in d.items():
    print(paar)

# Ausgabe sin die entsprechenden Tupel
    
# Liefert ein iterierbares Objekt, das alle Schlüssel durchläuft.
d.keys()

d = {'k1':'v1','k2':'v2','k3':'v3','k4':'v4'}
for key in d.keys():
    print(key)

# Beachte beim Kopieren wird zwar das Dictionary selbst kopiert, 
# es handelt sich aber bei den Werten um ein Referenz auf das gleich Objekt.
d1 = {'schluessel':[1,2,3]}
d2 = d1.copy()
d2['schluessel'].append(4)
>>> d2 = {'schluessel':[1,2,3,4]}
>>> d1 = {'schluessel':[1,2,3,4]}

# Diese Funktion löscht das Schlüssel-Werte Paar mit dem Schlüssel k und gibt den entsprechenden Wert zurück
d.pop()

# Es werden alle Values durchlaufen
d = {'k1':'v1','k2':'v2','k3':'v3','k4':'v4'}
for v in d.values():
    print(v)

```