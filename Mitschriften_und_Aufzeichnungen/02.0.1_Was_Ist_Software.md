# Was ist Software?

Der Begriff Software umfasst alle immateriellen Teile eines Computers.   
**Programme + Daten**

---


## EVA Prinzip

Eingabe -> Verarbeitung -> Ausgabe

---

## Arten von Software

1. Standard-Software (nicht quellcode offen, kann nicht angepasst werden z.B. Office, Betriebssysteme Windows)

2. Individualsoftware (Software, die auf Kundenwunsch erstellt worden ist.

3. Angepasste Standardsoftware (d.h. über eine programmspezifische Programmiersprache, kann ich Software um bestimmte Aufgaben programmieren / erweitern z.B. VBA, ABAP)

---

## Programmiersprachen Klassifizieren

Wir unterscheiden Programmiersprachen nach der historischen Entwicklung und ein anderes Mal nach der Programmiertechnik.

### Historische Entwicklung:

1. Ersten Generation:   
   Maschinensprache (Maschinencode)  
   Hierbei werden die Operationen ausschließlich aus Nullen und Einsen eingegeben.  
   Nachteil: Sehr unübersichtlich in der Programmierung.


2. Zweite Generation:   
   Assembler  
   Assemblersprachen besitzen Operationskürzel, wie z.B. Sprungbefehle, Addition, Kopierbefehle.  
   Diese werden dann vom Assembler in Maschinen-Code übersetzt.  Ist jedoch immer an einem Prozessortyp gebunden.


3. Dritte Generation:  
   Prozedurale Sprachen  
   Diese Sprachen sind weitgehend unabhängig von einem Computersystem, man bezeichnet sie auch als "höhere Programmiersprachen"  
   **Nachteil:** Ist der hohe Speicherplatzverbrauch.  
   **Beispiel:** C, C++, Pascal, Basic, Java, Python


4. Vierte Generation:  
   Generation Languages
   Diese Art von Sprachen beschreibt, ein Problem, ohne den genauen algorithmischen Weg anzugeben.  
   Eine einzelne Anweisung löst eine Folge von internen Einzelschritten aus.  
   z.B. SQL, OpenAccess


5. Fünfte Generation:  
   künstliche Intelligenz  
   Für diese Problematik sind spezielle Programmiersprachen entwickelt worden.  
   Sie versuchen unter bestimmten Bedingungen menschliche Verhaltensweisen nachzuahmen.  
   z.B. Prolog, Lisp, Smalltalk


## Programmiertechnik
1. **Prozedurale Sprachen**  
Damit bezeichnen wir Programmiersprache, die die gestellten Probleme als Folge von Anweisungen lösen.
Diese Anweisungen werden sequentiell abgearbeitet.

    ```python
   Programmstart

        Anweisung 1
        Anweisung 2
        Anweisung 3
        ...
    Programmende
   ```

Hierbei ist keine Zusammenfassung von Funktionalität und Daten möglich.

### 2.) Objektorientierte Sprachen
Zeitaufwendig ist die Erstellung der Struktur, deshalb wird diese Art von Programmiertechnik bei größeren Projekten angewendet.  
"Visual Paradigm" zur Erstellung von UML-Diagrammen.  

Zeitlichen Einordnung:   
1970 begannen Techniker diese Art von Programmiertechnik zu entwickeln.  
In der OOP werden Funktionalität und Daten gekapselt. Das hat den Vorteil, dass wir Programmteile (Klassen) leicht wiederverwenden können.  
Beispiele: C++, Java, C#

### 3.) Hybride Sprachen
Diese Art von Sprachen vereinen beide Ansätze. Man kann sie prozedural als auch objektorientiert einsetzen.  
In der Regel sind diese Sprachen Interpretersprachen.

* **Interpreter Sprachen**  
Quellcode/ Programm --> Interpreter wertet die Befehle während der Laufzeit aus. --> Ausführung auf dem Prozessor  


* **Compiler Sprache**
Quellcode/ Programm --> Compiler übersetzt den Quellcode in Maschinencode bevor das Programm ausgeführt werden kann. --> Ausführung auf dem Prozessor

Bei diesen Sprachen ist eine strikte Trennung nicht möglich.  
Beispiel: JavaScript, Python, PHP

### 4.) Funktionale Sprachen
Bei dieser Art von Sprachen ist das Programm eine Funktion.  
Diese Funktion kann natürlich auch untergeordnete Funktionen oder ander Funktionen aufrufen  
Beispiel: LISP, Prolog

### 5.) Skriptsprachen
Siehe hybride Sprachen

### 6.) Logischen Programmiersprachen
Hier wird kein Algorithmus zum Lösen des Problems angegeben, sondern es werden lediglich Bedingungen für eine Lösung definiert.  
Erstmalig wurde diese Art von Sprachen 1970 entwickelt.  
Beispiel: PROLOG (Programming in LOGic)

### 7.) Erziehungsorientierte Programmiersprachen
Diese Sprachen helfen jungen Menschen die Programmierung näherzubringen,  
häufig auf spielerische und bildliche Art.  
Beispiel: Scratch