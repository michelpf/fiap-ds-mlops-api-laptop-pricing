import joblib
import json
import requests

def get_model_version():
    response = requests.get('https://api.github.com/repos/michelpf/fiap-ds-mlops-laptop-pricing/tags')
    data = response.json()
    
    filtered_tags = [tag for tag in data if 'laptop-pricing@v' in tag['name']]
    sorted_tags = sorted(filtered_tags, key=lambda k: k['name'])
    latest_tag_name = sorted_tags[-1]['name']
    
    return latest_tag_name

model = joblib.load("model.pkl")
model_version = get_model_version()

def handler(event, context):

    data = event["data"]
    print(data)  
    
    data_processed = prepare_payload(data)
    prediction = model.predict([data_processed])

    print(prediction)

    return {  
        'statusCode': 200,
        'prediction': int(prediction[0]),
        'version': model_version
    }




def prepare_payload(data):

    data_processed = []

    data_processed.append(1) if data["brand"] == "asus" else data_processed.append(0)
    data_processed.append(1) if data["brand"] == "dell" else data_processed.append(0)
    data_processed.append(1) if data["brand"] == "hp" else data_processed.append(0)
    data_processed.append(1) if data["brand"] == "lenovo" else data_processed.append(0)
    data_processed.append(1) if data["brand"] == "other" else data_processed.append(0)

    data_processed.append(1) if data["processor_brand"] == "amd" else data_processed.append(0)
    data_processed.append(1) if data["processor_brand"] == "intel" else data_processed.append(0)
    data_processed.append(1) if data["processor_brand"] == "m1" else data_processed.append(0)
    
    data_processed.append(1) if data["processor_name"] == "core i3" else data_processed.append(0)
    data_processed.append(1) if data["processor_name"] == "core i5" else data_processed.append(0)
    data_processed.append(1) if data["processor_name"] == "core i7" else data_processed.append(0)
    data_processed.append(1) if data["processor_name"] == "other" else data_processed.append(0)
    data_processed.append(1) if data["processor_name"] == "ryzen 5" else data_processed.append(0)
    data_processed.append(1) if data["processor_name"] == "ryzen 7" else data_processed.append(0)
    
    data_processed.append(1) if data["os"] == "other" else data_processed.append(0)
    data_processed.append(1) if data["os"] == "windows" else data_processed.append(0)
    
    data_processed.append(1) if data["weight"] == "casual" else data_processed.append(0)
    data_processed.append(1) if data["weight"] == "gaming" else data_processed.append(0)
    data_processed.append(1) if data["weight"] == "thinnlight" else data_processed.append(0)

    data_processed.append(1) if data["warranty"] == "0" else data_processed.append(0)
    data_processed.append(1) if data["warranty"] == "1" else data_processed.append(0)
    data_processed.append(1) if data["warranty"] == "2" else data_processed.append(0)
    data_processed.append(1) if data["warranty"] == "3" else data_processed.append(0)

    data_processed.append(1) if data["touchscreen"] == "0" else data_processed.append(0)
    data_processed.append(1) if data["touchscreen"] == "1" else data_processed.append(0)
    
    data_processed.append(1) if data["ram_gb"] == "4" else data_processed.append(0)
    data_processed.append(1) if data["ram_gb"] == "8" else data_processed.append(0)
    data_processed.append(1) if data["ram_gb"] == "16" else data_processed.append(0)
    data_processed.append(1) if data["ram_gb"] == "32" else data_processed.append(0)

    data_processed.append(1) if data["hdd"] == "0" else data_processed.append(0)
    data_processed.append(1) if data["hdd"] == "512" else data_processed.append(0)
    data_processed.append(1) if data["hdd"] == "1024" else data_processed.append(0)
    data_processed.append(1) if data["hdd"] == "2048" else data_processed.append(0)

    data_processed.append(1) if data["ssd"] == "0" else data_processed.append(0)
    data_processed.append(1) if data["ssd"] == "128" else data_processed.append(0)
    data_processed.append(1) if data["ssd"] == "256" else data_processed.append(0)
    data_processed.append(1) if data["ssd"] == "512" else data_processed.append(0)
    data_processed.append(1) if data["ssd"] == "1024" else data_processed.append(0)
    data_processed.append(1) if data["ssd"] == "2048" else data_processed.append(0)
    data_processed.append(1) if data["ssd"] == "3072" else data_processed.append(0)

    data_processed.append(1) if data["graphic_card"] == "4" else data_processed.append(0)
    data_processed.append(1) if data["graphic_card"] == "8" else data_processed.append(0)
    data_processed.append(1) if data["graphic_card"] == "16" else data_processed.append(0)
    data_processed.append(1) if data["graphic_card"] == "32" else data_processed.append(0)

    data_processed.append(1) if data["ram_type"] == "ddr4" else data_processed.append(0)
    data_processed.append(1) if data["ram_type"] == "other" else data_processed.append(0)

    data_processed.append(1) if data["os_bit"] == "32" else data_processed.append(0)
    data_processed.append(1) if data["os_bit"] == "64" else data_processed.append(0)

    return data_processed
