# Repetitionsfragen Tag 1

1. **Was ist Software?**
	>A: Alle immateriellen Bestandteile eines Computersystems (Programme und Daten)
	
2. **Zu welcher Gruppe von Programmiersprachen gehört Python?**
	>A: Zu der Gruppe der hybriden Programmiersprache (OOP und prozedural)
	
3. **Wann wurde Python entwickelt?**
	>A: in den 90ger Jahren
	
4. **Von wem wurde Python entwickelt**
	>A: Von dem Niederländer Guido von Rossum
	
5. **Muss die Groß und Kleinschreibung von Variablennamen in Python beachtet werden?**
	>A: Ja, Python ist "Case-Sensitiv"
	
6. **Können einmal geschriebene Python-Programme auf unterschiedlichen Plattformen laufen?**
	>A: Ja, Python ist Plattformunabhängig
	
7. **Welche Kontrollstrukturen unterscheiden wir?**
	>A: Verzweigungen und Schleifen
	
8. **Wie lautet die allgemeine Syntax der if-Verzweigung**
	>A: if Bedingung:
		Anweisung
		
9. **Wie lautet die allgemeine Form der while-Schleife?**
	>A: while Bedingung:
		Anweisung
		
10. **Was macht der % Operator**
	>A: Er berechnet den Restwert einer Division

11. **Mit welcher Funktion kann ich ein Element einer Liste hinzufüge**
	>A: inert() und append()
 
12. **Mit welcher Syntax kann ich eine Liste definieren?**
	> A: Mit eckigen Klammern, in denen die Elemente kommagetrennt aufgelistet werden.

13. **Welche Wirkung hat die >>break<< Anweisung?**
    > A: An der Stelle, an der die Anweisung auftritt, wird die Schleife abgebrochen.

14. **Welche Wirkung hat die continue Anweisung?**
    > A: An der Stelle, wo die continue Anweisung auftritt, werden alle nachfolgenden Befehle in der Schleife ignoriert  
	> und es wird in die nächste Wiederholung der Schleife an den Schleifenkopf gesprungen.
	
15. **Was bedeutet die >>elif<< Anweisung**
	> A: Diese Anweisung ist eine Kurzform von else if.  
	> Damit ist es möglich eine zusätzliche Bedingung zu prüfen  
	> Wenn die Bedingung zutrifft, werden folgende elif ignoriert

16. **Mit welcher Funktion kann ich die Länge einer Liste ermitteln?**
	> A: Mit der len() Funktion

17. **Mit welcher Funktion kann ich Benutzereingaben realisieren?**
	> A: Mit der input() Funktion

18. **Mit welcher Funktion kann ich ein Element einer Liste entfernen?**
	> A: Mit der remove(/) Funktion

19. Mit welcher Funktion kann ich prüfen, ob sich ein Element in einer Liste befindet?**
    > A: Mit der index() Funktion

20. **Wann verwende ich in der Regel die for-Schleife?**
	> A: Wenn, ich die Anzahl der Wiederholungen kenne.

21. **Wann verwende ich in der Regel die while-Schleife?**
    > A: Wenn ich die Anzahl der Wiederholungen nicht kenne

22. **Welche Parameter kenne Sie bzgl. der print() Funktion**
	> * end 
    > * sep 
    > * file
23. **Was kann der Parameter end bei der print() Funktion bewirken?**
	> A: Er definiert das Enden einer Ausgabe. Standard ist ein Zeilenumbruch.
24. **Was bewirkt der Parameter sep bei der print() Funktion?**
	> A: Er definiert den Trenner zwischen den auszugebenden Werten.
25. **Wie kann ich die Ausgabe auf eine Datei umleiten?**
    > A. Indem ich eine neue Datei öffne, die Variable der Ausgabekanalkennung (fielHandler) als den Wert des Parameters file der print() Funktion zuweise.
26. **Was ist der Unterschied zwischen einer Liste und einem Tupel**
    > * Ein Tupel ist unveränderbar.
    > * Klammerung bei der Liste ist eine eckige Klammerung
27. **Wo startet ein Index bei einer sequenziellen Liste?**
    > A: Bei 0
28. **Mit welcher Methode kann ich einen String oder Abschnitt eines String in eine Liste überführen?**
    > A: mit der split() Funktion
29. **Mit welcher Funktion kann ich eine Zufallszahl erzeugen?**
    > A: Mit der z.B. randint() Funktion des Moduls random
30. **Was ist der Unterschied zwischen sortierten und unsortierten Listen / Mengen**
    > A: Sortierte Listen verfügen über einen Index, über den ich jedes Element ansprechen kann.  
	> Die Reihenfolge bleibt stets erhalten,  
	> was bei unsortierten Listen nicht der Fall ist.
31. **Mit welcher Funktion kann ich mit ein iterierbaren Objekt über alle Schlüssel-Werte-Paare eines Dictionary's zurückgeben lassen?**
    > A: Mit der items() Funktion
32. **Durch welche Eigenschaften ist ein set in Python charakterisiert?**
    > A: Ist eine ungeordnete, aus einmaligen, Elementen.
33. **Wie wird ein set in der Syntax definiert?**
	> A: mit geschweiften Klammern, in der die Elemente aufgezählt werden 
34. **Mit welcher Funktion kann ich ein set erzeugen?**
	> A: Mit der Set() Funktion
35. **Mit welcher Funktion kann ich den Datentyp einer Variable prüfen**
    > A: Mit der type() Funktion
36. **Wie erzeuge ich eine Menge von unveränderlichen Elementen?**
    > A: Mit der Funktion frozenset()
37. **Mit welcher Funktion kann ich Elemente einem set hinzufügen?**
    > A: Mit der add() Funktion
38. **Wie definiere ich eine selbstdefinierte Funktion in Python?**
    > A: def funktionsname(ParameterListe):
	> 	Anweisung
	> 	(option return parameter)
39. **Wie kann ich Standardwerte für Funktionsparameter festlegen?**
    > A: Indem ich in der Funktionsdefinition den Parametern dich ein >>=<< den entsprechenden Standardwert zuweise.
40. **Was sind lokale Variablen?**
    > Lokale Variablen sin Variablen, die innerhalb von Funktionen definiert werden und auch nur dort gültig sind.
41. **Was sind globale Variablen?**
    > A: Globale Variablen sind Variablen, die ausserhalb von Funktionen definiert sind und sowohl in Funktionen uns außerhalb von Funktionen gültig sind.
42. **Was ist der Unterschied zwischen Klassen und Objekten?**
	> Eine Klasse ist das Template (Vorlage)... ein Objekt ist eine instantiierte Klasse
43. Was ist der Unterschied zwischen einer Funktion und einer Methode?
    > Funktionell: Keiner  
	> Funktionen heißen Methoden, wenn sie in einer Klasse definiert wurden
44. Was ist der Unterschied zwischen einer Klassenvariablen und einer Instanzvariablen?
    > Klassenvariablen sind in jedem Objekt verfügbar.  
	> Instanzvariablen sind einem Objekt zugeordnet und erst nach einer instantiierung einer Klasse verfügbar.
45. Gibt es Unterschiede ind er Zugriffsart auf Klassenvariablen im Zustand "Klasse" un im Zustand "Objekt"?
    > Sobald eine Klasse instantiiert wurde, MUSS mit dem Klassennamen auf die Variable zugegriffen werden.  
	> Im Zustand als Klasse ist das nicht notwendig
46. Wenn in einer Klasse eine statische Methode vorhanden ist, muss auch diese bei einer Instantiierung den Klassennamen voranstellen,
	wenn auf eine Klassenvariable zugegriffen wird?
    > Es muss nicht gemacht werden, das die Methode in der Klasse verbleibt.
	>> Aber: Da wir sicherstellen wollen, dass wir keinen Fehler erhalten, sprechen wir Klassenvariablen IMMER über den Klassennamen an!!
47. ```python
    OBJ_MyClass.variable = 10
    ```
    1. Was passiert, wenn die Instanzvariable noch nicht vorhanden ist?
    2. Was passiert, wenn eine gleichnamige Klassenvariable vorhanden ist?
    > zu i. Sie wird erstellt  
	> zu ii. Sie wird trotzdem erstellt
48. Was ist ein "Setter"?
    > Eine Methode in einer Klasse, die von außen genutzt werden soll um eine Instanzvariable zu setzen.
	> Das Gegenteil ist der Getter, der angesprochen werden soll, um eine kontrollierte Ausgabe von Instanzvariablen zu erhalten.
49. Was ist "self" und ist "self" fix oder kann "self" umbenannt werden?
    > Natürlich kann in Python "self" umbenannt werden.  
	> Sollte aber nicht getan werden, da es eine "Best Practice" darstellt und wir in unserer Programmierung
	> übergreifend eine Gemeinsame Benennung haben sollten.  
	> Ist eine Referenz auf das Objekt selbst