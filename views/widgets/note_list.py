import json

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.base import runTouchApp
from kivy.uix.scrollview import ScrollView
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, BaseListItem, MDList, OneLineListItem
from kivy.uix.label import Label
from views.note_screen import NoteScreen

Builder.load_file('views/widgets/kv/note_list.kv')

class NoteList(BoxLayout):

    def moveScreen(self, screen_name, note_id):
      ns = NoteScreen()
      ns.note(note_id)
      App.get_running_app().switch_screen(screen_name)

    def __init__(self, *args, **kwargs):

      self.ml = MDList()
      self.root = BoxLayout()
      self.sv = ScrollView(
        pos_hint={'top': 1.62},
        size_hint_y=1.5,
      )

      self.sv.clear_widgets()

      super(NoteList, self).__init__(**kwargs)

      try:
        with open('models/data.json', 'r') as get_data:
          pass
      except IOError as e:
        label = Label(
          text="Not note please add new note",
          font_size='16pt',
          pos_hint={'top': 2.05},
          color=(1,1,1,1)
        )
        self.add_widget(label)
      else:
        with open('models/data.json', 'r') as get_data:
          data = json.loads(get_data.read())

          for item in data:
            self.ml.add_widget(
              OneLineListItem(
                  text=item['name'],
                  id=str(item['id']),
                  theme_text_color='Custom',
                  text_color=(1,1,1,1),
                  on_press=lambda x: self.moveScreen('note', x.id)
              )
            )
          self.sv.add_widget(self.ml)  
          self.add_widget(self.sv)
  
