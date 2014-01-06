# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
import gtk
import random


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

WHITE_NOTES = ("C", "D", "E", "F", "G", "A", "B")
BLACK_NOTES = ("C#", "D#", "F#", "G#", "A#", "Db", "Eb", "Gb", "Ab", "Bb")
ALL_NOTES = WHITE_NOTES + BLACK_NOTES


class Task:

    def __init__(self, callback):
        self.currTask = TASKS[0][0]
        self.callback = callback
        vb = gtk.VBox(False, 5)
        vb.set_border_width(10)
        radio = None
        for (k, v) in TASKS:
            radio = gtk.RadioButton(radio, v)
            radio.connect("toggled", self.__onSelect, k)
            vb.pack_start(radio, expand=False)

        scroll = gtk.ScrolledWindow()
        scroll.set_size_request(100, 150)
        scroll.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
        scroll.add_with_viewport(vb)

        self.btnStart = gtk.Button("Start")
        self.btnStart.connect("clicked", self.__start)

        vb2 = gtk.VBox(False, 10)
        vb2.set_border_width(10)
        vb2.pack_start(scroll, expand=False)
        vb2.pack_start(self.btnStart, expand=False)

        self.view = gtk.Frame("Task")
        self.view.set_size_request(250, 230)
        self.view.add(vb2)

    def __onSelect(self, widget, data):
        self.currTask = data

    def __start(self, widget):
        self.callback()

    def nextNote(self):
        octave = 1
        if self.currTask in ("w2", "b2"):
            octave = 2
        elif self.currTask in ("w3", "b3"):
            octave = 3
        elif self.currTask in ("w4", "b4"):
            octave = 4
        elif self.currTask in ("wl", "bl"):
            octave = random.randint(1, 2)
        elif self.currTask in ("wr", "br"):
            octave = random.randint(3, 5)
        else:
            octave = random.randint(1, 5)

        note = ""
        if self.currTask == "all":
            note = random.choice(ALL_NOTES)
        elif self.currTask[0:1] == "w":
            note = random.choice(WHITE_NOTES)
        else:
            note = random.choice(BLACK_NOTES)

        return (octave, note)
