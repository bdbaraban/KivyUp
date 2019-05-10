#!/usr/bin/env python3
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


class KivyUp(App):
    def build(self):
        self.layout = GridLayout(cols=2)
        self.box = BoxLayout(orientation='horizontal', spacing=20)
        self.txt = TextInput(hint_text='Write here')
        self.btn = Button(text='Convert', on_press=self.clearText)
        self.box.add_widget(self.txt)
        self.box.add_widget(self.btn)
        self.box2 = BoxLayout(orientation='horizontal', spacing=20)
        self.txt2 = TextInput(hint_text='converted here')
        self.box2.add_widget(self.txt2)
        self.layout.add_widget(self.box)
        self.layout.add_widget(self.box2)
        return self.layout

    def clearText(self, instance):
        self.txt.text = ''


KivyUp().run()
