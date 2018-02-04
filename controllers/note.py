import json
import random
import os

class Note():

  def run(self, notename, notetext):

    note = {
      'id': random.randint(1,1000),
      'name': notename,
      'text': notetext
    }

    def get_targetNote(self):
      return self.target_note

    try:
      with open('models/data.json') as get_data:
        pass
    except IOError as e:
      with open('models/data.json', 'w') as get_data:
        notes = []
        notes.append(note)
        get_data.write(json.dumps(notes))
    else:
      with open('models/data.json', 'r') as get_data:
        File = get_data.read()
        parse_file = json.loads(File)
        parse_file.append(note)

        with open('models/data.json', 'w') as get_data:
          get_data.write(json.dumps(parse_file))

  def getDataFromID(self, note_id):
    id_note = int(note_id)
    try:
      with open('models/data.json', 'r') as get_data:
        pass
    except IOError as e:
      print('Нет такой ноды')
    else:
      with open('models/data.json', 'r') as get_data:
        data = json.loads(get_data.read())
        for items in data:
          if items['id'] == int(note_id):
            self.target_note = {
              'id': items['id'],
              'name': items['name'],
              'text': items['text']
            }

  def delete_note(self):
    try:
      with open('models/data.json', 'r') as get_data:
        pass
    except IOError as e:
      print('not node')
    else:
      with open('models/data.json', 'r') as get_data:
        data = json.loads(get_data.read())
        for items in data:
          if items['id'] == self.target_note['id']:
            data.remove(items)
            with open('models/data.json', 'w') as get_data:
              get_data.write(json.dumps(data))
              if len(data) == 0:
                os.remove('models/data.json')