# Annotations
z.B. My_Int : int = 200 -> wird akzeptiert oder ignoriert.

Das werden wir auch für unsere Module erst dann machen können, wenn das in Python implementiert ist.

Seit Python 3.7 könne wir jedoch auf Klassenebene einen Zwang implementieren, diese Annotations zu berücksichtigen.  

````python
from datatclass import dataclass

@dataclass()
class MyClass():
````
Duch _@dataclass_ als Dekorator baut eine Kapselung um meine Klasse auf. D.H jede Annotation wird jetzt durch den Compiler zwangsweise an die dataclass übergeben.  
Jetzt haben wir eine Datenprüfung.

_dataclass()_ bietet auch die Möglichkeit, Variablen als "unmutable" zu kennzeichnen (also nicht veränderbar)