#!/usr/bin/python3
"""Entry point of app."""
from kivy.app import App
from screen_manager.manager import presentation


class WRITEMEmd(App):
    def build(self):
        return presentation


WRITEMEmd().run()