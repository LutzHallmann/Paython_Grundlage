# Unsere "Hallo Welt" als GUI-Klasse
import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import  ttk    # tkinter beinhaltet widgets, dabei
                            # wurde 2007 ttk als Bibliothek für "modernere Widgets hinzugefügt

class Windows(tk.Tk)
    def __init__(self):
        super().__init__(self)  # Wir müssen auch die Elternklasse instantiieren, damit wir auf die Instanzvariablen und Methoden zugreifen könne
        self.title('Meine erste GUI-Klasse')
        self.geometry('300x100')    # Angabe der Größe des Windows in Pixel
        self.button = ttk.Button(self.master), text='Ende', command=(self.__ende__)
            # statt einer Methode. könne wir auch self.quit() aufrufen
            # eine Elternmethode
        self.button.pack(side='left')

        self.slogan = ttk.Button(self.master, text='Hallo', command=self.write_slogan)
        self.slogan.pack()

