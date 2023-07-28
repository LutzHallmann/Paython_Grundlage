"""
"Hallo Welt" als GUI
"""
import tkinter  # das Paket für alle Klassen der GUI

# wir haben für unseren Button ein Command hinterlegt, das natürlich als Funktion auch defieniert werden muss
def ende():
    main.destroy()

# Erstellen eines Hauptfensters
main = tkinter.Tk() # TK ist das Hauptfenster oder auch Root-Widget genannt
main.title('Meine erste GUI')   # Eine Eigenschaft des Hauptfensters festlegen

# In unserem Window eine Ausgabe erzeugen - ein einfaches Label
MyLabel1 = tkinter.Label(main, text='Hallo Welt... und Danke für den Fisch')    # Label -> die Klasse für Textfelder
                                                                                # 1. Parameter  -> Muss-Parameter -> in welchem Fensterobjekt soll das Label erzeugt werden
                                                                                # Jeder weitere Parameter ist eine "named" Parameter wie z.B. Text
MyLabel1['font'] = 'Courier 16 italic'  # Schriftart für das Textfeld
MyLabel1['height'] = 2
MyLabel1['width'] = 100

# Wir müssen unser Label-Objekt in das Hauptfenster mit aufnehmen
MyLabel1.pack()

# Im ersten Schritt mussten wir unser Fenster "hart" schließen,
# jetzt ein Button der das für uns übernimmt
MyButton1 = tkinter.Button(main, text='Beenden', command=ende)  # Button für "main"
                                                                # test -> Beschriftung des Buttons
                                                                # command -> was soll beim klicken des Buttons passieren - Funktion oder Methode
                                                                # Das wird auch "Callback-Funktion" genannt
                                                                # Achtung!! Normalerweise werden Funktionen und Methoden mit () aufgerufen,
                                                                # das ist hier nicht der Fall
MyButton1['fg'] = 'red'
MyButton1.pack()

main.mainloop() # Starten des Fensters in einer Endlosschleife
