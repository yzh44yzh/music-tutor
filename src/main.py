#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
import gtk
import keyboard

def onClose(widget, event, data = None):
    gtk.main_quit()
    return False

w = gtk.Window(gtk.WINDOW_TOPLEVEL)
w.set_title("Hello :)")
w.set_border_width(10)
w.connect("delete_event", onClose)

kb = keyboard.create()
w.add(kb)
w.show_all()

gtk.main()
