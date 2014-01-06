# -*- coding: utf-8 -*-

import settings
import stave
import keyboard


class MainController:
    
    def __init__(self):
        pass


    def init(self, staveInst, keyboardInst, settingsInst):
        self.stave = staveInst
        self.keyboard = staveInst
        self.settings = settingsInst


    def onChangeSettings(self, showNotes):
        self.keyboard.showNotes(showNotes)

    
    def onNote(self, note):
        self.stave.showNote(note)
