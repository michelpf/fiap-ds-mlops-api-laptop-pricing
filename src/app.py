"""
Função para executar predição de valor de laptop com base nos parâmetros enviados, 
como modelo, processador, memória etc.
Utiliza modelo que precisa ser baixado do repositório de registro de modelos em toda 
implantação nova.
"""

from datetime import datetime
import joblib
import boto3


model = joblib.load("model.pkl")

with open("model_version.txt", 'r', encoding='utf8') as file:
    model_version = file.read()

cloudwatch = boto3.client("cloudwatch")


def write_real_data(data, prediction):
    """
    Função para escrever os dados consumidos para depois serem estudados 
    para desvios de dados, modelo ou conceito.

    Args:
        data (dict): dicionário de dados com todos os atributos.
        prediction (int): valor de predição
    """

    now = datetime.now()
    now_formatted = now.strftime("%d-%m-%Y %H:%M")

    file_name = f"{now.strftime('%Y-%m-%d')}_laptop_prediction_data.csv"

    data["price"] = prediction
    data["timestamp"] = now_formatted
    data["model_version"] = model_version

    s3 = boto3.client("s3")
    bucket_name = "fiap-ds-mlops"
    s3_path = "laptop-prediction-real-data"

    try:
        existing_object = s3.get_object(Bucket=bucket_name, Key=f'{s3_path}/{file_name}')
        existing_data = existing_object['Body'].read().decode('utf-8').strip().split('\n')
        existing_data.append(','.join(map(str, data.values())))
        updated_content = '\n'.join(existing_data)

    except s3.exceptions.NoSuchKey:
        updated_content = ','.join(data.keys()) + '\n' + ','.join(map(str, data.values()))


    s3.put_object(Body=updated_content, Bucket=bucket_name, Key=f'{s3_path}/{file_name}')

def input_metrics(data, prediction):
    """
    Função para escrever métricas customizadas no Cloudwatch.

    Args:
        data (dict): dicionário de dados com todos os atributos.
        prediction (int): valor de predição.
    """

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
                'Dimensions': [{'Name': key, 'Value': str(value)}]
            },
        ], Namespace='Laptop Pricing Features')



def handler(event, context=False):
    """
    Função principal de execução da API no Lambda

    Args:
        event (json): payload para processamento.
        context (json): dados adicionais ao contexto (opcional).

     Returns:
        json: Predição de preço.
    """

    print(event)
    print(context)

    data = event["data"]
    print(data)

    data_processed = prepare_payload(data)
    prediction = model.predict([data_processed])

    prediction = int(prediction[0])
    print("Prediction: " + str(prediction))

    input_metrics(data, prediction)
    write_real_data(data, prediction)

    return {
        'statusCode': 200,
        'prediction': int(prediction),
        'version': model_version
    }


def prepare_payload(data):
    """
    Função para padronizar o payload de entrada de modo a 
    ser compatível com a execução do modelo.

    Args:
        data (dict): dicionário de dados com todos os atributos.

     Returns:
        dict: payload padronizado.

    """

    data_processed = []

    data_processed.append(int(data["ram_gb"]))
    data_processed.append(int(data["ssd"]))
    data_processed.append(int(data["hdd"]))
    data_processed.append(int(data["graphic_card"]))
    data_processed.append(int(data["warranty"]))

    conditions = {
        "brand": {"asus", "dell", "hp", "lenovo", "other"},
        "processor_brand": {"amd", "intel", "m1"},
        "processor_name": {"core i3", "core i5", "core i7", "other", "ryzen 5", "ryzen 7"},
        "os": {"other", "windows"},
        "weight": {"casual", "gaming", "thinnlight"},
        "touchscreen": {"0", "1"},
        "ram_type": {"ddr4", "other"},
        "os_bit": {"32", "64"}
    }

    for key, values in conditions.items():
        for value in values:
            data_processed.append(1 if data[key] == value else 0)

    return data_processed
