# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
import gtk
import octave


def __onClick(widget, data = None):
    print "click", data


def create():
    octaves = [octave.create(num, __onClick) for num in range(1, 6)]
    hb = gtk.HBox(False, 10)
    [hb.pack_start(oc, False) for oc in octaves]
    return hb

