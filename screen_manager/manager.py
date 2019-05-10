#!/usr/bin/env python3
"""Defines the screen manager classes."""
import os.path
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import FadeTransition, ScreenManager, Screen


class ReadMeScreen(Screen):
    writeText = ObjectProperty(None)
    def textPrint(self):
        print(self.writeText.text)


class WriteMeScreen(Screen):
    textBlock = ObjectProperty(None)
    def textHarvest(self):
        print(self.textBlock.text)


class ScreenManagement(ScreenManager):
    shared_text = StringProperty("")


presentation = Builder.load_file(os.path.join(os.path.dirname(__file__),
                                              "screens.kv"))
rms = ReadMeScreen()
rms.textPrint()
