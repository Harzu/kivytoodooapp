import json

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.base import runTouchApp
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, BaseListItem, MDList, OneLineListItem

Builder.load_file('views/widgets/kv/note_list.kv')

class NoteList(BoxLayout):

    ml = MDList(
      pos_hint={'top': 1.65}
    )
    root = BoxLayout()



    def __init__(self, *args, **kwargs):
        super(NoteList, self).__init__(**kwargs)

        try:
          with open('models/data.json', 'r') as get_data:
            pass
        except IOError as e:
          print('Нет данных попробуйте добавить новую заметку')
        else:
          with open('models/data.json', 'r') as get_data:
            data = json.loads(get_data.read())
            for item in data:
              self.ml.add_widget(
                OneLineListItem(
                    text=item['name']
                )
              )
            self.add_widget(self.ml)
  
