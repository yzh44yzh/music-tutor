# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
import gtk
import octave


class Keyboard:

    def __init__(self, callback):
        self.callback = callback
        self.__octaves = [octave.Octave(num, self.__onClick)
                          for num in range(1, 6)]
        self.view = gtk.HBox(False, 2)
        [self.view.pack_start(oc.view, False) for oc in self.__octaves]

    def __onClick(self, widget, data):
        self.callback(data)

    def showNotes(self, show):
        [oc.showNotes(show) for oc in self.__octaves]
