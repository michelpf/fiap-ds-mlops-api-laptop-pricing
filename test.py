import src.app as app
import json

with open('data.json') as data_file:
  data = data_file.read()

data = json.loads(data)

event = {}
event["data"] = data

evento = json.dumps(event)
print(event)

app.handler(event, "")