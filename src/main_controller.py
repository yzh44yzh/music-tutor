# -*- coding: utf-8 -*-

import task
import stave
import keyboard
import settings
import octave
import notes
from os import system

class MainController:

    def __init__(self):
        pass


    def init(self, taskInst, staveInst, keyboardInst, settingsInst):
        self.currNote = None
        self.task = taskInst
        self.stave = staveInst
        self.keyboard = keyboardInst
        self.settings = settingsInst
        self.midiListener = MidiEventListener(self)
        self.midiListener.start()


    def start(self):
        self.__nextNote()


    def onChangeSettings(self, showNotes):
        self.keyboard.showNotes(showNotes)


    def onNote(self, note):
        print("note %s %s" % note)
        if note == self.currNote:
            self.__nextNote()
        else:
            (oc, key) = note
            if key in notes.MATCHING_KEYS:
                note = (oc, notes.MATCHING_KEYS[key])
            if note == self.currNote:
                self.__nextNote()
            else:
                print("Error: need %s but got %s" % (self.currNote, note))
                self.notifyError()


    def __nextNote(self):
        nextNote = self.task.nextNote()
        while nextNote == self.currNote:
            nextNote = self.task.nextNote()
        self.currNote = nextNote
        self.stave.showNote(self.currNote)


    def notifyError(self):
        # TODO need a better way to play sound :)
        system("mplayer assets/sound/error.wav > /dev/null 2>&1")
        pass

    def onClose(self):
        self.midiListener.stop()



import string
import threading
import subprocess

class MidiEventListener(threading.Thread):

    def __init__(self, controller):
        threading.Thread.__init__(self)
        self.controller = controller
        self.__midiData = None
        self.__needStop = threading.Event()


    def run(self):
        self.__midiData = subprocess.Popen(["aseqdump", "-p", "20:0"], stdout = subprocess.PIPE)
        while True:
            if(self.__needStop.isSet()):
                self.__needStop.clear()
                self.__midiData.terminate()
                break
            event = self.__midiData.stdout.readline()
            if "Note on" in event:
                # event is "20:0   Note on                 0, note 62, velocity 66"
                s1 = string.split(event, ",")[1] # " note 62"
                s2 = string.split(s1, " ")[2]    # "62"
                note = notes.parse(int(s2))
                self.controller.onNote(note)


    def stop(self):
        self.__needStop.set()
