# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
import gtk
import random


TASKS = (("right_white", "right hand, whites only"),
         ("right",       "right hand"),
         ("left_white",  "left hand, whites only"),
         ("left",        "left hand"),
         ("all",         "All keys"))

WHITE_NOTES = ("C", "D", "E", "F", "G", "A", "B")
BLACK_NOTES = ("C#", "D#", "F#", "G#", "A#", "Db", "Eb", "Gb", "Ab", "Bb")

NOTES = {"right_white": tuple([(2, "A"), (2, "B")]
                              + map(lambda n: (3, n), WHITE_NOTES)
                              + map(lambda n: (4, n), WHITE_NOTES)
                              + map(lambda n: (5, n), WHITE_NOTES)),
         "right":       tuple([(2, "A"), (2, "B"), (2, "A#"), (2, "Ab"), (2, "Bb")]
                              + map(lambda n: (3, n), WHITE_NOTES + BLACK_NOTES)
                              + map(lambda n: (4, n), WHITE_NOTES + BLACK_NOTES)
                              + map(lambda n: (5, n), WHITE_NOTES + BLACK_NOTES)),
         "left_white":  tuple(map(lambda n: (1, n), WHITE_NOTES)
                              + map(lambda n: (2, n), WHITE_NOTES)),
         "left":        tuple(map(lambda n: (3, n), WHITE_NOTES + BLACK_NOTES)
                              + map(lambda n: (4, n), WHITE_NOTES + BLACK_NOTES))}


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
        scroll.set_size_request(100, 165)
        scroll.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
        scroll.add_with_viewport(vb)

        self.btnStart = gtk.Button("Start")
        self.btnStart.connect("clicked", self.__start)

        vb2 = gtk.VBox(False, 10)
        vb2.set_border_width(10)
        vb2.pack_start(scroll, expand=False)
        vb2.pack_start(self.btnStart, expand=False)

        self.view = gtk.Frame("Task")
        self.view.set_size_request(250, 245)
        self.view.add(vb2)

    def __onSelect(self, widget, data):
        self.currTask = data

    def __start(self, widget):
        self.btnStart.set_label("Stop")
        self.callback()

    def nextNote(self):
        notes = ()
        if self.currTask == "all":
            notes = NOTES["right"] + NOTES["left"]
        else:
            notes = NOTES[self.currTask]
        return random.choice(notes)


    def clear(self):
        self.btnStart.set_label("Start")
