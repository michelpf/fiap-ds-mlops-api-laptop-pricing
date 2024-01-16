import src.app as app
import json
import time
import random
from dotenv import load_dotenv
import requests
import os

load_dotenv()

def consume_service(data):
  
  endpoint = os.getenv("API_ENDPOINT")
  api_key = os.getenv("API_KEY")

  headers = {'x-api-key': api_key, 'Content-Type': 'application/json'}

  response = requests.post(endpoint, data=json.dumps(data), headers=headers)

  print(response.status_code)
  print(response.text)
  
  if response.status_code == 200:
      result = (response.json())
      print(result)


with open('data.json') as data_file:
  data = data_file.read()

data = json.loads(data)

event = {}
event["data"] = data

evento = json.dumps(event)
print(event)

brand = ["asus", "dell", "hp", "lenovo", "other"]
process_brand = ["amd", "intel", "m1"]
processor_name = ["core i3", "core i5", "core i7", "other", "ryzen 5", "ryzen 7"]
operation_system = ["other", "windows"]
weight = ["casual", "gaming", "thinnlight"]
#warranty = ["0", "1", "2", "3"]
warranty = random.randrange(0, 5, 1)
touchscreen = ["0", "1"]
#ram_gb = ["4", "8", "16", "32"]
ram_gb = random.randrange(4, 256, 4)
#hdd = ["0", "512", "1024", "2048"]
hdd = random.randrange(0, 8000, 512)
#ssd = ["0", "128", "256", "512", "1024", "2048", "3072"]
ssd = random.randrange(0, 4000, 512)
#graphic_card = ["4", "8", "16", "32"]
graphic_card = random.randrange(4, 256, 3)
ram_type = ["ddr4", "other"]
os_bit = ["32", "64"]




while True:

  ssd_v = 0
  hdd_v = random.randrange(0, 8000, 512)
  if hdd_v == 0:
    ssd_v = random.randrange(0, 4000, 512)
    if ssd_v == 0:
      ssd_v = ssd[0]

  process_brand_v = random.choice(process_brand)

  if process_brand_v == "m1":
    brand_v = "other"
    processor_name_v = "other"
    os_v = "other"
    weight_v = "thinnlight"
    touchscreen_v = "0"
    ram_gb_v = random.choice(["8", "16", "24"])
    graphic_card_v = "8"
    ram_type_v="other"
    os_bit_v = "64"
    ssd_v = random.choice(["256", "512"])
    hdd_v == "0"
  else:
    brand_v = random.choice(brand)
    processor_name_v = random.choice(processor_name)
    os_v = random.choice(operation_system)
    weight_v = random.choice(weight)
    touchscreen_v = random.choice(touchscreen)
    ram_gb_v =  random.randrange(4, 256, 4)
    graphic_card_v = graphic_card = random.randrange(4, 256, 4)
    ram_type_v = random.choice(ram_type) 
    os_bit_v = random.choice(os_bit) 


  event["data"] = {
    "brand": brand_v,
    "processor_brand": process_brand_v,
    "processor_name": processor_name_v,
    "os": os_v,
    "weight": weight_v,
    "warranty": int(random.randint(0, 5)),
    "touchscreen": touchscreen_v,
    "ram_gb": ram_gb_v,
    "hdd": int(hdd_v),
    "ssd": ssd_v,
    "graphic_card": graphic_card_v,
    "ram_type": ram_type_v,
    "os_bit": os_bit_v
 }

  app.handler(event, "")  
  #consume_service(event)  
  #time.sleep(random.uniform(1, 30))