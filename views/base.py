import json

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.scrollview import ScrollView

Builder.load_file('views/kv/base.kv')

class ScreenBase(Screen):

  sv = ScrollView()

  def add_note(self, screen_name):
    App.get_running_app().switch_screen(screen_name)