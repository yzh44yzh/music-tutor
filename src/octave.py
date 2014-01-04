# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
import gtk

whiteClr = gtk.gdk.Color(red=65535, green=65535, blue=65535)
blackClr = gtk.gdk.Color(red=0, green=0, blue=0)


def __createBtn(note, num, callback, color):
    b =  gtk.Button("")
    b.set_size_request(30, 80)

    b.modify_bg(gtk.STATE_NORMAL, color)
    b.modify_bg(gtk.STATE_PRELIGHT, color)
    b.connect("clicked", callback, note + str(num))
    return b


def __createRow(notes, num, callback, color):
    btns = [__createBtn(note, num, callback, color) for note in notes]
    hb = gtk.HBox(False, 5)
    [hb.pack_start(b, expand=False) for b in btns]
    return hb


def create(num, callback):
    hb1 = __createRow(["#A", "#B", "#C", "#D"], num, callback, blackClr)
    hb2 = __createRow(["A", "B", "C", "D"], num, callback, whiteClr)
    vb = gtk.VBox(False, 10)
    vb.pack_start(hb1, False)
    vb.pack_start(hb2, False)
    return vb

