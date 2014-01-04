# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
import gtk

whiteClr = gtk.gdk.Color(red=65535, green=65535, blue=65535)
blackClr = gtk.gdk.Color(red=0, green=0, blue=0)

whiteKeys = ("C", "D", "E", "F", "G", "A", "B")
blackKeys1 = ("C#", "D#")
blackKeys2 = ("F#", "G#", "A#")


def __createBtn(color, note, callback):
    b =  gtk.Button("")
    if color == whiteClr:
        b.set_size_request(30, 140)
    else:
        b.set_size_request(26, 80)

    b.modify_bg(gtk.STATE_NORMAL, color)
    b.modify_bg(gtk.STATE_PRELIGHT, color)
    b.connect("clicked", callback, note)
    return b


def __createRow(keys, color, num, callback, spacing = 2):
    btns = [__createBtn(color, note + str(num), callback) for note in keys]
    hb = gtk.HBox(False, spacing)
    [hb.pack_start(b, expand=False) for b in btns]
    return hb


def __createBlacks(num, callback):
    row1 = __createRow(blackKeys1, blackClr, num, callback, 6)
    row2 = __createRow(blackKeys2, blackClr, num, callback, 6)
    fx = gtk.Fixed()
    fx.put(row1, 16, 0)
    fx.put(row2, 32 * 3 + 16, 0)
    return fx


def create(num, callback):
    whites = __createRow(whiteKeys, whiteClr, num, callback)
    blacks = __createBlacks(num, callback)
    fx = gtk.Fixed()
    fx.put(whites, 0, 0)
    fx.put(blacks, 0, 0)
    return fx

