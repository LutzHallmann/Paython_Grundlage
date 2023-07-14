# Sets
Der Datentyp **set** ist seit der BVersion 2.4 in Python enthalten.  
Ein Set enhält eine ungeordnete Menge von eindeutigen und unveränderlichen Elementen.  
Jedes Element darf nicht mehrmals vorkommen.

```python
staedte = {'Hamburg','Berlin','Freiburg'}

'Berlin' in staedte
>>> True
```
> Python merkt an den fehlenden Doppelpunkten, dass es sich nicht um Dictionary handelt, sondern um ein Set.

Wenn wir Tupelelemente in der set() Funktion aufführen und innerhalb der Tupel sich doppelte Einträge befinden, werden dies bereinigt.

```python
staedte = set(('Hamburg','Berlin','Freiburg','Berlin')) # Berlin verschwindet in der Ausgabe des set.
print(staedte)                                          # Es wird in die Funktion "Set" ein Tupel gepackt und somit als Set umgewandelt
>>>{'Hamburg','Berlin','Freiburg'}
```
Um Elemente einem set hinzuzufügen, verwenden wir die add() Funktion  
Alle Elemetne werden mit der Funtkion clear() gelöscht.  
Ausgewählte Elemente werden mit der Funktion remove(), falls diese existieren gelöscht.  
Wenn diese nicht existieren wird eine Fehlermeldung ausgegeben.
```python
staedte = {'Hamburg','Berlin','Freiburg'}
staedte.remove('Berlin')
```