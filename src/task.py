# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
import gtk


TASKS = (("w3", "White keys, 3rd octave"),
         ("w4", "White keys, 4th octave"),
         ("w2", "White keys, 2nd octave"),
         ("wl", "White keys, left hand"),
         ("wr", "White keys, right hand"),
         ("wa", "All white keys"),
         ("b3", "Black keys, 3rd octave"),
         ("b4", "Black keys, 4th octave"),
         ("b2", "Black keys, 2nd octave"),
         ("bl", "Black keys, left hand"),
         ("br", "Black keys, right hand"),
         ("ba", "All black keys"),
         ("all", "All keys"))


class Task:

    def __init__(self):
        vb = gtk.VBox(False, 5)
        vb.set_border_width(10)
        radio = None
        for (k, v) in TASKS:
            radio = gtk.RadioButton(radio, v)
            vb.pack_start(radio, expand=False)

        scroll = gtk.ScrolledWindow()
        scroll.set_size_request(100, 150)
        scroll.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
        scroll.add_with_viewport(vb)

        btn = gtk.Button("Start")

        vb2 = gtk.VBox(False, 10)
        vb2.set_border_width(10)
        vb2.pack_start(scroll, expand=False)
        vb2.pack_start(btn, expand=False)

        self.view = gtk.Frame("Task")
        self.view.set_size_request(250, 230)
        self.view.add(vb2)
