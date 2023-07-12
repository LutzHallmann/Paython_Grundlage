# Tupel

Rein Formal unterscheiden sich Tupel von Listen durch die Syntax der runden Klammer

```python
y = (3,99,"Ein Text")

# Ein Tupel kann auch ohne runden Klammern erzeugt werden
y = 2,99,"Ein Text"
```
**Der Unterschied zu Listen ist der, dass ein Tupel nicht mehr verändert werden kann.**  
Es könne keine Elemente aus diesem Tupel entfernt werden oder hinzugefügt werden.

## Unpacking
```python
tupel = ('Hamburg','Berlin','München')
stadt1, stadt2, stadt2 = tupel
```