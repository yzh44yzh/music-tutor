#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
import gtk
import main_controller
import settings
import stave
import keyboard


def onClose(widget, event, data = None):
    gtk.main_quit()
    return False

w = gtk.Window(gtk.WINDOW_TOPLEVEL)
w.set_title("Hello :)")
w.set_border_width(10)
w.connect("delete_event", onClose)

_controller = main_controller.MainController()
_settings = settings.Settings(_controller.onChangeSettings)
_stave = stave.Stave()
_keyboard = keyboard.Keyboard(_controller.onNote)
_controller.init(_stave, _keyboard, _settings)

hb = gtk.HBox(False, 20)
hb.pack_start(_settings.view, False)
hb.pack_start(_stave.view, False)

vb = gtk.VBox(False, 20)
vb.pack_start(hb, False)
vb.pack_start(_keyboard.view, False)

w.add(vb)
w.show_all()
_stave.clear()

gtk.main()
