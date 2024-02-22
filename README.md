[![Build and Push to ECR](https://github.com/michelpf/fiap-ds-mlops-api-laptop-pricing/actions/workflows/deploy.yml/badge.svg)](https://github.com/michelpf/fiap-ds-mlops-api-laptop-pricing/actions/workflows/deploy.yml)

# API de Predição de Preço de Laptops

Serviço para predição de preço de laptop baseado em determinadas características, como marca, procesador, armazenamento e etc.

Utilizado modelo basedo em container, implementado no modelo serverless utilizando AWS Lambda.

## Modo de utilização

O handler da API espera entrada de dados no formato JSON, como no exemplo as seguir:

```json
{
  "data": {
    "brand": "dell",
    "processor_brand": "intel",
    "processor_name": "core i5",
    "os": "windows",
    "weight": "casual",
    "warranty": "2",
    "touchscreen": "0",
    "ram_gb": "16",
    "hdd": "0",
    "ssd": "256",
    "graphic_card": "8",
    "ram_type": "ddr4",
    "os_bit": "64"
  }
}
```

## Possibilidades de valores

brand = ["asus", "dell", "hp", "lenovo", "other"]  (categoric)
processor_brand = ["amd", "intel", "m1"] (categoric)
processor_name = ["core i3", "core i5", "core i7", "other", "ryzen 5", "ryzen 7"] (categoric)
os = ["other", "windows"] (categoric)
weight = ["casual", "gaming", "thinnlight"] (categoric)
warranty = ["0", "1", "2", "3"] (numeric)
touchscreen = ["0", "1"] (categoric)
ram_gb = ["4", "8", "16", "32"] (numeric)
hdd = ["0", "512", "1024", "2048"] (numeric)
ssd = ["0", "128", "256", "512", "1024", "2048", "3072"] (numeric)
graphic_card = ["4", "8", "16", "32"] (numeric)
ram_type = ["ddr4", "other"] (categoric)
os_bit = ["32", "64"] (categoric)





Todos os parâmetros precisam ser enviados, obrigatoriamente.

O resultado é retornado no formato JSON, informando o valor da predição e a versão do modelo.

```json
{
  "statusCode": 200,
  "prediction": 55198,
  "version": "linear_regression@v1.0.0"
}
```

## Uso

Este repositório possui os seguintes módulos:

* Teste de unidade na pasta ```tests``` implementado com [Pytest](https://docs.pytest.org/en/7.4.x/).
Os testes avaliam a integridade do modelo, parâmetros de entrada, versionamento, dentre outros. 

* Arquivo de montagem do container Docker, contendo as instruções para empacotamento da imagem incluindo dependências e o modelo.

* O arquivo ```test.py``` é uma forma rápida para interagir com o código sem necessitar montar uma imagem. Permite depurar o código localmente mais facilmente.
