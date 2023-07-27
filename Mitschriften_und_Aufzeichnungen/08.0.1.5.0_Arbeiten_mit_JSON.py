"""
Arbeiten mit JSON

Python mcht das arbeiten mit JSON sehr leicht.

json.dump(Objekt)   ->  erzeugt ein JSON-Objekt
json.load(Zeichkette)    -> erzeugt einen Python Datentypen
"""
import json

LIS_Liste1 = list(range(1,5))
LIS_Liste2 = list(range(10,15))
DICT_MiyDict = {'name' : 'abc äöüß', 'Liste1' : LIS_Liste1, 'Liste2' : LIS_Liste2}

print(json.dumps(DICT_MiyDict)) # Defaultmäßig stellt der JSON-Dump alle Zeichen außerhalb des ASCII-Bereichs als Unicode-Zeichen da.

print(json.dumps(DICT_MiyDict, ensure_ascii=False)) # Jetzt nicht mehr
print(json.dumps(DICT_MiyDict, ensure_ascii=False, indent=5)) # indent stellt Einrückungen dar

# Datei schreib quick and dirty
dateihandler = open('08.0.1.5.1_myjson.txt', 'wt')
dateihandler.write(json.dumps(DICT_MiyDict, ensure_ascii=False))
dateihandler.close()

# Wir lesen die Datei wieder ein
dateihandler = open('08.0.1.5.1_myjson.txt', 'rt')
jsonObjekt = dateihandler.read()
print(json.loads(jsonObjekt))   # Hier muss es "json.loads" sein da das Objekt durchgecrawlt werden muss

# Andere Möglichkeit
print(json.load(open('08.0.1.5.1_myjson.txt', 'rt')))   # hier nur "json.load", da die ganze Datei direkt eingelesen wird

ufo = (json.load(open('08.0.1.5.1_myjson.txt', 'rt')))
print(isinstance(ufo, dict))# JSON hat uns wieder ein Dictionary erstellt

print(ufo['Liste1'])