import src.app as app
import json
import time
import random

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
os = ["other", "windows"]
weight = ["casual", "gaming", "thinnlight"]
warranty = ["0", "1", "2", "3"]
touchscreen = ["0", "1"]
ram_gb = ["4", "8", "16", "32"]
hdd = ["0", "512", "1024", "2048"]
ssd = ["0", "128", "256", "512", "1024", "2048", "3072"]
graphic_card = ["4", "8", "16", "32"]
ram_type = ["ddr4", "other"]
os_bit = ["32", "64"]



while True:

  event["data"] = {
    "brand": random.choice(brand),
    "processor_brand": random.choice(process_brand),
    "processor_name": random.choice(processor_name),
    "os": random.choice(os),
    "weight": random.choice(weight),
    "warranty": random.choice(warranty),
    "touchscreen": random.choice(touchscreen),
    "ram_gb": random.choice(ram_gb),
    "hdd": random.choice(hdd),
    "ssd": random.choice(ssd),
    "graphic_card": random.choice(graphic_card),
    "ram_type": random.choice(ram_type),
    "os_bit": random.choice(os_bit) 
 }

  app.handler(event, "")  
  time.sleep(0.5)