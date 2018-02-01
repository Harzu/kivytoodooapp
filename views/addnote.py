from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.app import App

from views.widgets.input import InputNote
from controllers.add_note import Note

Builder.load_file('views/kv/addnote.kv')

class AddNote(Screen):
  
  def save_note(self, screen_name, note_name, note_body):
    controller_addnote = Note()
    controller_addnote.run(note_name, note_body)
    App.get_running_app().switch_screen(screen_name)