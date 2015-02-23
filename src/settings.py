# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
import gtk


class Settings:

    def __init__(self, callback):
        self.callback = callback
        cb = gtk.CheckButton("Show notes on keyboard")
        cb.set_active(False)
        cb.connect("toggled", self.__onChange, None)

        self.sb = gtk.SpinButton()
        self.sb.set_range(5, 100)
        self.sb.set_increments(5, 20)
        self.sb.set_value(50)
        lb = gtk.Label("Num notes per task")
        hb = gtk.HBox(False, 5)
        hb.pack_start(self.sb, expand=False)
        hb.pack_start(lb, expand=False)

        vb = gtk.VBox(False, 5)
        vb.set_border_width(10)
        vb.pack_start(hb, expand=False)
        vb.pack_start(cb, expand=False)

        self.view = gtk.Frame("Settings")
        self.view.set_size_request(250, 230)
        self.view.add(vb)

    def num_notes_per_task(self):
        return self.sb.get_value()

    def __onChange(self, widget, data=None):
        self.callback(widget.get_active())
