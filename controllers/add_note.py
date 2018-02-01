import json

class Note():

  def run(self, notename, notetext):

    note = {
      'name': notename,
      'text': notetext
    }

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