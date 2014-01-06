# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
import gtk

NOTE_POSITIONS = {(1, "C"): 29,
                  (1, "D"): 23,
                  (1, "E"): -51,
                  (1, "F"): -45,
                  (1, "G"): -39,
                  (1, "A"): -33,
                  (1, "B"): -27,
                  (2, "C"): 29, 
                  (2, "D"): 23,
                  (2, "E"): -51,
                  (2, "F"): -45,
                  (2, "G"): -39,
                  (2, "A"): -33,
                  (2, "B"): -27,
                  (3, "C"): 59, # TODO line -1
                  (3, "D"): 53,
                  (3, "E"): 47,
                  (3, "F"): 41,
                  (3, "G"): 35,
                  (3, "A"): 29,
                  (3, "B"): 23,
                  (4, "C"): -51,
                  (4, "D"): -45,
                  (4, "E"): -39,
                  (4, "F"): -33,
                  (4, "G"): -27,
                  (4, "A"): -21, # TODO line 6
                  (4, "B"): -15, # TODO line 6|7
                  (5, "C"): -9,  # TODO line 7
                  (5, "D"): -45,
                  (5, "E"): -39,
                  (5, "F"): -33,
                  (5, "G"): -27,
                  (5, "A"): -21, # TODO line 6
                  (5, "B"): -15} # TODO line 6|7

class Stave:
    
    def __init__(self):
        self.staveBg = gtk.Image()
        self.staveBg.set_from_file("assets/img/stave.png")
        self.treble_clef = gtk.Image()
        self.treble_clef.set_from_file("assets/img/treble_clef.png")
        self.bass_clef = gtk.Image()
        self.bass_clef.set_from_file("assets/img/bass_clef.png")
        self.note_1 = gtk.Image()
        self.note_1.set_from_file("assets/img/note_1.png")
        self.note_2 = gtk.Image()
        self.note_2.set_from_file("assets/img/note_2.png")
        self.lb8va = gtk.Label("8va")

        self.view = gtk.Fixed()
        self.view.put(self.staveBg, 0, 0)
        self.view.put(self.treble_clef, 10, 20)
        self.view.put(self.bass_clef, 10, 38)
        self.view.put(self.note_1, 10, 20)
        self.view.put(self.note_2, 10, 20)
        self.view.put(self.lb8va, 0, 0)


    def clear(self):
        self.treble_clef.hide()
        self.bass_clef.hide()
        self.note_1.hide()
        self.note_2.hide()
        self.lb8va.hide()

        
    def showNote(self, (octave, note)):
        if octave == 1 or (octave == 5 and note != "C"):
            self.lb8va.show()
        else:
            self.lb8va.hide()
            
        if octave < 3:
            self.treble_clef.hide()
            self.bass_clef.show()
        else:
            self.treble_clef.show()
            self.bass_clef.hide()

        y = NOTE_POSITIONS[(octave, note)]
        if y > 0:
            self.note_1.show()
            self.note_2.hide()
            self.view.move(self.note_1, 130, y)
        else:
            self.note_1.hide()
            self.note_2.show()
            self.view.move(self.note_2, 130, -y)

