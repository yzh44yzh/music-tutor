# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
import gtk
import octave


class Keyboard:
    
    def __init__(self):
        self.__octaves = []


    def __onClick(self, widget, data = None):
        print "click", data


    def create(self):
        boxes = []
        for num in range(1, 6):
            octaveComp = octave.Octave(num, self.__onClick)
            self.__octaves.append(octaveComp)
            box = octaveComp.create()
            boxes.append(box)

        hb = gtk.HBox(False, 2)
        [hb.pack_start(box, False) for box in boxes]
        return hb

    
    def showNotes(self, show):
        [octave.showNotes(show) for octave in self.__octaves]

