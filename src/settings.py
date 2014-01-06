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

        lb = gtk.Label("Language:")
        lb.set_alignment(0, 0)
        rbEn = gtk.RadioButton(None, "English")
        rbRu = gtk.RadioButton(rbEn, u"Русский")

        vb = gtk.VBox(False, 5)
        vb.set_border_width(10)
        vb.pack_start(cb, expand=False)
        vb.pack_start(lb, expand=False)
        vb.pack_start(rbEn, expand=False)
        vb.pack_start(rbRu, expand=False)

        self.view = gtk.Frame("Settings")
        self.view.add(vb)

    def __onChange(self, widget, data=None):
        self.callback(widget.get_active())
