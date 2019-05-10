#!/usr/bin/python3
"""Entry point of app."""
from kivy.app import App
from screen_manager.manager import presentation


class WRITEMEmd(App):
    """Main WRITEME.md Kivy app."""

    def build(self):
        """Build the screen manager."""
        return presentation


WRITEMEmd().run()
