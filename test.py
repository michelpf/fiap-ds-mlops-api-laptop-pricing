import json
import os

# Verifica se o arquivo está na pasta "src" ou na raiz do projeto
if os.path.exists("src/app.py"):
    import src.app as app
else:
    import app

with open('data.json') as data_file:
  data = data_file.read()

event = json.loads(data)

print(event)

app.handler(event, "")  
