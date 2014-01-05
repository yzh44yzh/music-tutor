# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
import gtk

WHITE_CLR = gtk.gdk.Color(red=65535, green=65535, blue=65535)
BLACK_CLR = gtk.gdk.Color(red=0, green=0, blue=0)

WHITE_KEYS = ("C", "D", "E", "F", "G", "A", "B")
BLACK_KEYS_1 = ("C#", "D#")
BLACK_KEYS_2 = ("F#", "G#", "A#")

class Octave:

    def __init__(self, num, callback):
        self.num = num
        self.callback = callback


    def __createBtn(self, color, note):
        b =  gtk.Button("")
        if color == WHITE_CLR:
            b.set_size_request(30, 140)
        else:
            b.set_size_request(26, 80)

        b.modify_bg(gtk.STATE_NORMAL, color)
        b.modify_bg(gtk.STATE_PRELIGHT, color)
        b.connect("clicked", self.callback, note)
        return b


    def __createRow(self, keys, color, spacing = 2):
        btns = [self.__createBtn(color, note + str(self.num)) for note in keys]
        hb = gtk.HBox(False, spacing)
        [hb.pack_start(b, expand=False) for b in btns]
        return hb


    def __createBlacks(self):
        row1 = self.__createRow(BLACK_KEYS_1, BLACK_CLR, 6)
        row2 = self.__createRow(BLACK_KEYS_2, BLACK_CLR, 6)
        fx = gtk.Fixed()
        fx.put(row1, 16, 0)
        fx.put(row2, 32 * 3 + 16, 0)
        return fx


    def create(self):
        whites = self.__createRow(WHITE_KEYS, WHITE_CLR)
        blacks = self.__createBlacks()
        fx = gtk.Fixed()
        fx.put(whites, 0, 0)
        fx.put(blacks, 0, 0)
        return fx

