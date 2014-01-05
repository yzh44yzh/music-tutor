# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
import gtk

STAVE_BG = gtk.Image()
STAVE_BG.set_from_file("assets/img/stave.png")

TREBLE_CLEF = gtk.Image()
TREBLE_CLEF.set_from_file("assets/img/treble_clef.png")

NOTE_1 = gtk.Image()
NOTE_1.set_from_file("assets/img/note_1.png")

NOTE_1_POS = {(3, "E"): 47,
              (3, "F"): 41}

class Stave:
    
    def __init__(self):
        self.view = gtk.Fixed()
        self.view.put(STAVE_BG, 0, 0)
        self.view.put(TREBLE_CLEF, 10, 20)
        self.showNote(3, "F")

        
    def showNote(self, octave, note):
        y = self.__get_pos(octave, note)
        self.view.put(NOTE_1, 130, y)


    def __get_pos(self, octave, note):
        return NOTE_1_POS[(octave, note)]
