#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
import gtk
import settings
import stave
import keyboard


def onClose(widget, event, data = None):
    gtk.main_quit()
    return False


def onChangeSettings(showNotes):
    _keyboard.showNotes(showNotes)
    

w = gtk.Window(gtk.WINDOW_TOPLEVEL)
w.set_title("Hello :)")
w.set_border_width(10)
w.connect("delete_event", onClose)

_settings = settings.Settings(onChangeSettings)
_stave = stave.Stave()
_keyboard = keyboard.Keyboard()

hb = gtk.HBox(False, 20)
hb.pack_start(_settings.view, False)
hb.pack_start(_stave.view, False)

vb = gtk.VBox(False, 20)
vb.pack_start(hb, False)
vb.pack_start(_keyboard.view, False)

w.add(vb)
w.show_all()

gtk.main()
