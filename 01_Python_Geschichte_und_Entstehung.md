# Python Geschichte und Entstehung

Die Programmiersprachen wurde Anfang der 90er Jahre entwickelt.  
Federführung hatte Guido von Rossum in Amsterdam.  
Der Name kommt von der britischen Komikertruppe Monty Python.

Zielsetzung war die Entwicklung einer Programmiersprache, die einfach ist - auch für Laien ohne Programmiererfahrung.  
Die Version 3.0 ist im Dezember 2008 erschienen. 
Die Unterstützung von Python 2 wurde 2020 beendet.

## Grundlegende Konzepte

Python vereint mehrere Programmierparadigmen.
* Objektorientiert
+ Funktional

Viele gängige Sprachelemente sind implementiert.

> **Das wichtigste Ziel eines Programms / Software ist es Redundanzen zu vermeiden**

Es handelt sich um eine Skriptsprache.  
Sie wird interpretiert.
Wie in Java oder C# verfügt Python über einen Compiler, der aus dem Quelltext ein Kompilat erzeugt -> Byte code.  
Dieser Byte code wird in einer "Virtuellen Maschine" genannt Python-Interpreter ausgeführt.

Quellcode / Programm --> Compiler übersetzt den Quellcode in ByteCode --> Ausführung im Python Interpreter --> Auf der Maschine ausführbaren Code.

Python ist aufgrund dieser Technik "plattformunabhängig", denn es ist möglich ein Python Programm auf alles Rechnern auszuführen, die über einen Python - Interpreter verfügen.

Ebenso haben wir mit der Python Installation eine Standardbibliothek.  
Hier sind Funktionen vordefiniert, die man arbeitszeit sparend einsetzen kann.

**Vorteile:**
* Python ist OpenSource, steht jedoch unter der PSF-Lizenz.
* Einfache Syntax
* Flexibel
* Erweiterbarkeit
* Python verfügt mittlerweile über umfangreiche Bibliotheken im Bereich KI
  * NumPy
  * SciPy
  * matplotlib
  * Tensorflow
  * PyTorch

**Nachteile:**  
Maschinennahe Programmierung nicht möglich.  
Zeitkritische Programme kann man in C schreiben un dann über Python API (Application Programming Interface) anbinden.

**Einsatzbeispiele:**
* Viele große Anwendungen sind in Python geschrieben:
  * Google Mail
  * DropBox
  * Reddit

* Erweiterungsmöglichkeiten von Standardsoftware:
  * Maya
  * Blender
  * Cinema4D
  * GIMP