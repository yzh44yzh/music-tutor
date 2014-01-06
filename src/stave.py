# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
import gtk

POS = (("up", 65),
       ("up", 59),
       ("up", 53),
       ("up", 47),
       ("up", 41),
       ("up", 35),
       ("up", 29),
       ("up", 23),
       ("down", 51),
       ("down", 45),
       ("down", 39),
       ("down", 33),
       ("down", 27),
       ("down", 21),
       ("down", 15),
       ("down", 9))

NOTE_POSITIONS = {(1, "C"): POS[6],
                  (1, "D"): POS[7],
                  (1, "E"): POS[8],
                  (1, "F"): POS[9],
                  (1, "G"): POS[10],
                  (1, "A"): POS[11],
                  (1, "B"): POS[12],
                  (2, "C"): POS[6], 
                  (2, "D"): POS[7],
                  (2, "E"): POS[8],
                  (2, "F"): POS[9],
                  (2, "G"): POS[10],
                  (2, "A"): POS[11],
                  (2, "B"): POS[12],
                  (3, "C"): POS[1],
                  (3, "D"): POS[2],
                  (3, "E"): POS[3],
                  (3, "F"): POS[4],
                  (3, "G"): POS[5],
                  (3, "A"): POS[6],
                  (3, "B"): POS[7],
                  (4, "C"): POS[8],
                  (4, "D"): POS[9],
                  (4, "E"): POS[10],
                  (4, "F"): POS[11],
                  (4, "G"): POS[12],
                  (4, "A"): POS[13],
                  (4, "B"): POS[14],
                  (5, "C"): POS[15],
                  (5, "D"): POS[9],
                  (5, "E"): POS[10],
                  (5, "F"): POS[11],
                  (5, "G"): POS[12],
                  (5, "A"): POS[13],
                  (5, "B"): POS[14]}

class Stave:
    
    def __init__(self):
        self.staveBg = gtk.Image()
        self.staveBg.set_from_file("assets/img/stave.png")
        self.line_1 = gtk.Image()
        self.line_1.set_from_file("assets/img/line.png")
        self.line_2 = gtk.Image()
        self.line_2.set_from_file("assets/img/line.png")
        self.line_3 = gtk.Image()
        self.line_3.set_from_file("assets/img/line.png")
        self.line_4 = gtk.Image()
        self.line_4.set_from_file("assets/img/line.png")
        self.treble_clef = gtk.Image()
        self.treble_clef.set_from_file("assets/img/treble_clef.png")
        self.bass_clef = gtk.Image()
        self.bass_clef.set_from_file("assets/img/bass_clef.png")
        self.note_1 = gtk.Image()
        self.note_1.set_from_file("assets/img/note_1.png")
        self.note_2 = gtk.Image()
        self.note_2.set_from_file("assets/img/note_2.png")
        self.sharp = gtk.Image()
        self.sharp.set_from_file("assets/img/sharp.png")
        self.flat = gtk.Image()
        self.flat.set_from_file("assets/img/flat.png")
        self.lb8va = gtk.Label("8va")

        self.view = gtk.Fixed()
        self.view.put(self.staveBg, 0, 0)
        self.view.put(self.treble_clef, 10, 20)
        self.view.put(self.bass_clef, 10, 38)
        self.view.put(self.line_1, 130, 111)
        self.view.put(self.line_2, 130, 99)
        self.view.put(self.line_3, 130, 27)
        self.view.put(self.line_4, 130, 15)
        self.view.put(self.note_1, 10, 20)
        self.view.put(self.note_2, 10, 20)
        self.view.put(self.sharp, 0, 0)
        self.view.put(self.flat, 0, 0)
        self.view.put(self.lb8va, 0, 0)


    def clear(self):
        self.treble_clef.hide()
        self.bass_clef.hide()
        self.line_1.hide()
        self.line_2.hide()
        self.line_3.hide()
        self.line_4.hide()
        self.note_1.hide()
        self.note_2.hide()
        self.sharp.hide()
        self.flat.hide()
        self.lb8va.hide()

        
    def showNote(self, (octave, note)):
        self.clear()
        if octave == 1 or (octave == 5 and note != "C"):
            self.lb8va.show()
            
        if octave < 3:
            self.bass_clef.show()
        else:
            self.treble_clef.show()

        position = NOTE_POSITIONS[(octave, note[0:1])]
        if position == POS[0]:
            self.line_1.show()
            self.line_2.show()
            
        if position == POS[1]:
            self.line_2.show()

        if position == POS[13] or position == POS[14]:
            self.line_3.show()

        if position == POS[15]:
            self.line_3.show()
            self.line_4.show()

        (direction, y) = position
        half_y = y
        if direction == "up":
            self.note_1.show()
            self.view.move(self.note_1, 133, y)
            half_y = y + 28
        else:
            self.note_2.show()
            self.view.move(self.note_2, 133, y)
            half_y = y - 5
            
        half = note[1:2]
        if half == "#":
            self.sharp.show()
            self.view.move(self.sharp, 115, half_y)
            
        if half == "b":
            self.flat.show()
            self.view.move(self.flat, 115, half_y - 7)

