import json

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.app import App

from controllers.note import Note

Builder.load_file('views/kv/note_screen.kv')

class NoteScreen(Screen):

  nt = Note()

  def getData(self):
    print(json.dumps(self.nt.get_targetNote()))
    # if name != None:
    #   return name
    # else:
    #   return text

  def undo_screen(self, screen_name):
    App.get_running_app().switch_screen(screen_name)

  def delete(self, screen_name):
    self.nt.delete_note()
    App.get_running_app().switch_screen(screen_name)

  def note(self, note_id):
    self.nt.getDataFromID(note_id)