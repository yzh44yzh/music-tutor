#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
import gtk
import settings
import keyboard


def onClose(widget, event, data = None):
    gtk.main_quit()
    return False


def onChangeSettings(showNotes):
    keyboardComp.showNotes(showNotes)
    

w = gtk.Window(gtk.WINDOW_TOPLEVEL)
w.set_title("Hello :)")
w.set_border_width(10)
w.connect("delete_event", onClose)

settingsBox = settings.Settings(onChangeSettings).create()
keyboardComp = keyboard.Keyboard()
keyboardBox = keyboardComp.create()

vb = gtk.VBox(False, 20)
vb.pack_start(settingsBox, False)
vb.pack_start(keyboardBox, False)

w.add(vb)
w.show_all()

gtk.main()
