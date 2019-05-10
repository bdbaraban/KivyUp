#!/usr/bin/env python3
"""Defines the screen manager classes."""
import os.path
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class WriteMeScreen(Screen):
    """Screen for writing WRITME.md syntax."""
    pass


class ReadMeScreen(Screen):
    """Screen for converted markdown."""
    pass


class ScreenManagement(ScreenManager):
    """Main screen manager."""
    pass


presentation = Builder.load_file(os.path.join(os.path.dirname(__file__),
                                 "screens.kv"))
