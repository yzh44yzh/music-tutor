# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
import gtk


class Settings:


    def __init__(self, callback):
        self.callback = callback


    def __onChange(self, widget, data = None):
        self.callback(widget.get_active())


    def create(self):
        cb = gtk.CheckButton("Show notes on keyboard")
        cb.set_active(True)
        cb.connect("toggled", self.__onChange, None)
        cb.set_border_width(10)

        fr = gtk.Frame("Settings")
        fr.add(cb)

        return fr

