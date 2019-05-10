#!/usr/bin/python3
"""Entry point of app."""
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screen_manager.manager import presentation, WriteMeScreen, ReadMeScreen


#presentation

class WRITEMEmd(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WriteMeScreen())
        sm.add_widget(ReadMeScreen())
        return sm


WRITEMEmd().run()
