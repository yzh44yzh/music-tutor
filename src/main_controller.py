# -*- coding: utf-8 -*-

import task
import stave
import keyboard
import settings


class MainController:

    def __init__(self):
        pass

    def init(self, taskInst, staveInst, keyboardInst, settingsInst):
        self.currNote = None
        self.task = taskInst
        self.stave = staveInst
        self.keyboard = keyboardInst
        self.settings = settingsInst

    def start(self):
        self.currNote = self.task.nextNote()
        self.stave.showNote(self.currNote)

    def onChangeSettings(self, showNotes):
        self.keyboard.showNotes(showNotes)

    def onNote(self, note):
        if note == self.currNote:
            nextNote = self.task.nextNote()
            while nextNote == self.currNote:
                nextNote = self.task.nextNote()
            self.currNote = nextNote
            self.stave.showNote(self.currNote)
        else:
            self.notifyError()

    def notifyError(self):
        # TODO
        pass
