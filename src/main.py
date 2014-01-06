#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
import gtk
import main_controller
import task
import stave
import settings
import keyboard


def onClose(widget, event, data=None):
    gtk.main_quit()
    return False

w = gtk.Window(gtk.WINDOW_TOPLEVEL)
w.set_title("Music Tutor")
w.set_border_width(10)
w.connect("delete_event", onClose)

_controller = main_controller.MainController()
_task = task.Task(_controller.start)
_stave = stave.Stave()
_settings = settings.Settings(_controller.onChangeSettings)
_keyboard = keyboard.Keyboard(_controller.onNote)
_controller.init(_task, _stave, _keyboard, _settings)

hb = gtk.HBox(False, 10)
hb.pack_start(_task.view, expand=False)
hb.pack_start(_stave.view, expand=True, fill=True)
hb.pack_start(_settings.view, expand=False)

vb = gtk.VBox(False, 10)
vb.pack_start(hb, False)
vb.pack_start(_keyboard.view, False)

w.add(vb)
w.show_all()
_stave.clear()

gtk.main()
