# -*- coding: utf-8 -*-

import task
import stave
import keyboard
import settings
import octave
import notes
from os import system
import pygame

class MainController:

    def __init__(self):
        pass


    def init(self, taskInst, staveInst, keyboardInst, settingsInst):
        pygame.init()
        self.currNote = None
        self.noteCounter = 0
        self.maxNotes = 5 # 50

        self.task = taskInst
        self.stave = staveInst
        self.keyboard = keyboardInst
        self.settings = settingsInst
        self.midiListener = MidiEventListener(self)
        self.midiListener.start()
        self.okSound = pygame.mixer.Sound('assets/sound/ok.wav')
        self.errorSound = pygame.mixer.Sound('assets/sound/error.wav')


    def start(self):
        if(self.currNote is None):
            self.__nextNote()
        else:
            self.stop()


    def stop(self):
        self.noteCounter = 0
        self.currNote = None
        self.stave.clear()
        self.task.clear()


    def onChangeSettings(self, showNotes):
        self.keyboard.showNotes(showNotes)


    def onNote(self, note):
        if self.currNote is None: return

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
        self.okSound.play() # TODO play note

        nextNote = self.task.nextNote()
        while nextNote == self.currNote:
            nextNote = self.task.nextNote()
        self.currNote = nextNote

        self.noteCounter += 1
        if self.noteCounter > self.maxNotes:
            self.stop()
        else:
            self.stave.update(self.currNote, self.noteCounter, self.maxNotes)


    def notifyError(self):
        self.errorSound.play()


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
