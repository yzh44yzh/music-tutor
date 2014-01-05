# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
import gtk


class Settings:


    def __init__(self, callback):
        self.callback = callback
        cb = gtk.CheckButton("Show notes on keyboard")
        cb.set_active(True)
        cb.connect("toggled", self.__onChange, None)
        cb.set_border_width(10)

        self.view = gtk.Frame("Settings")
        self.view.add(cb)


    def __onChange(self, widget, data = None):
        self.callback(widget.get_active())

