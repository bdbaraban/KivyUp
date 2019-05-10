#!/usr/bin/env python3
"""Defines the screen manager classes."""
import os.path
from kivy.lang import Builder
from kivy.uix.screenmanager import FadeTransition, ScreenManager, Screen


class WriteMeScreen(Screen):
    pass


class ReadMeScreen(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file(os.path.join(os.path.dirname(__file__), "screens.kv"))