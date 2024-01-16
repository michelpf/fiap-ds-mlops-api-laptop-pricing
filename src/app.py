import joblib
import boto3
from datetime import datetime

model = joblib.load("model.pkl")
model_version = conteudo = open("model_version.txt", 'r').read()

cloudwatch = boto3.client("cloudwatch")


def write_real_data(data, prediction):
    file_name = f"{datetime.now().strftime('%Y-%m')}_laptop_prediction_data.csv"
    data["price"] = prediction
    
    s3 = boto3.client("s3")
    bucket_name = "fiap-ds-mlops"
    s3_path = "laptop-prediction-real-data"

    try:
        existing_object = s3.get_object(Bucket=bucket_name, Key=f'{s3_path}/{file_name}')
        existing_data = existing_object['Body'].read().decode('utf-8').strip().split('\n')
        existing_data.append(','.join(map(str, data.values())))
        updated_content = '\n'.join(existing_data)
    except s3.exceptions.NoSuchKey:
        # Se o arquivo não existir, cria um novo
        updated_content = ','.join(data.keys()) + '\n' + ','.join(map(str, data.values()))


    s3.put_object(Body=updated_content, Bucket=bucket_name, Key=f'{s3_path}/{file_name}')

    

def input_metrics(data, prediction):
    cloudwatch.put_metric_data(
        MetricData = [
            {
                'MetricName': 'Price Prediction',
                'Value': prediction,
                'Dimensions': [{'Name': "Currency", 'Value': "INR"}]
            },
        ], Namespace='Laptop Pricing Model')

    for key, value in data.items():
         cloudwatch.put_metric_data(
        MetricData = [
            {
                'MetricName': 'Latptop Feature ',
                'Value': 1,
                'Unit': 'Count',
                'Dimensions': [{'Name': key, 'Value': value}]
            },
        ], Namespace='Laptop Pricing Features')



def handler(event, context):

    print(event)
      
    data = event["data"]
    print(data)  
    
    data_processed = prepare_payload(data)
    prediction = model.predict([data_processed])

    print(prediction)

    prediction = int(prediction[0])

    input_metrics(data, prediction)
    write_real_data(data, prediction)

    return {  
        'statusCode': 200,
        'prediction': int(prediction),
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
