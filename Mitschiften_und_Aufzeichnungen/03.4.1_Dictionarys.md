# Dictionarys
**Dictionary's sind veränderbar!**  
Hier können wir Zuordnungen von Schlüsseln und Werte speichern (Key-Value-Paaren)
Key-Value Paar werden durch ":" getrennt.  
Die Liste wird in geschweifte Klammer geschrieben.  
z.B. d={"k1":"w1","k2":"w2"}

> Dictionary -> dict  

Ein Dictionary enthält beliebig viele Schlüssel-Werte-Paare (key-value pairs).  
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
# es handelt sich aber bei den Werten um eine Referenz auf das gleiche Objekt.
d1 = {'schluessel':[1,2,3]}
d2 = d1.copy()
d2['schluessel'].append(4)
>>> d2 = {'schluessel':[1,2,3,4]}
>>> d1 = {'schluessel':[1,2,3,4]}

# Diese Funktion löscht das Schlüssel-Werte-Paar mit dem Schlüssel k und gibt den entsprechenden Wert zurück
d.pop()

# Es werden alle Values durchlaufen
d = {'k1':'v1','k2':'v2','k3':'v3','k4':'v4'}
for v in d.values():
    print(v)

```
In Python gibt es zwei Arten, wie man eine Kopie eines vorhandenen Objektes erstellen kann.
1. Durch Zuweisen "="
2. Durch Verwenden von copy()

Der Unterschied zwischen beiden hängt davon ab, ob man eine tiefe Kopie oder eine flache Kopie des Objektes erstellen möchte.

> * zu 1.) Wenn mann eine Variable einer anderen Variable zuweist, erstellen Sie keine neue Kopie.  
> * Sie erstellen nur eine Referenz auf das ursprüngliche Objekt.  
> * Das bedeutet, dass Änderungen, die man an einer Variable vornimmt, sich auf die anderen auswirkt, wil beide auf die gleiche Speicherstelle / Objekt zeigen.
>   * liste1 = [1,2,3]
>   * liste2 = liste1
>   * liste2.append(4)
>   * print(liste1) # Ausgabe [1,2,3,4]

> * zu 2.) Die copy() Funktion erstellt eine "flache Kopie" des Objektes.  
> Das bedeutet, dass sie ein neues Objekt erstellt, das eine Kopie der ursprünglichen Elemente enthält.  
> Aber wenn die Elemente des Objektes selbst veränderbare Listen oder Wörterbücher sind, dann werden diese Elemente nicht kopiert, sondern referenziert
>   * liste1 = [1,2,[3,4]]
>   * liste2 = copy(liste1)
>   * liste2.append(5)
>   * print(liste1) # Ausgabe [1,2,[3,4,5]]

>* Wenn Sie eine tiefe Kopie erstellen möchten, bei der auch veränderbare Elemente kopiert werden,  
>kann man die Funktion deepcopy() verwenden.  
>YDamit ist sichergestellt, dass das ursprüngliche Objekt in keiner Weise durch Änderungen am kopierten Objekt beinflusst wird.
>  * liste1 = [1,2,[3,4]]
>  * liste2 = deepcopy(liste1)
>  * liste2.append(5)
>  * print(liste1) # Ausgabe [1,2,[3,4]]