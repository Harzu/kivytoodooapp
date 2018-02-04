from kivy.uix.screenmanager import ScreenManager, SlideTransition
from views.base import ScreenBase
from views.addnote import AddNote
from views.note_screen import NoteScreen
sm = ScreenManager(transition=SlideTransition())
screens = {
  'base':ScreenBase,
  'add':AddNote,
  'note':NoteScreen
}