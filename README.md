[![Build and Push to ECR](https://github.com/michelpf/fiap-ds-mlops-api-laptop-pricing/actions/workflows/deploy.yml/badge.svg)](https://github.com/michelpf/fiap-ds-mlops-api-laptop-pricing/actions/workflows/deploy.yml)

# API Laptop Pricing

Serviço para predição de preço de laptop baseado em determinadas características, como marca, procesador, armazenamento e etc.

Utilizado modelo basedo em container, implementado no modelo serverless utilizando AWS Lambda.

## Modo de utilização

O handler da API espera entrada de dados no formato JSON, como no exemplo as seguir:

json```
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

Todos os parâmetros precisam ser enviados, obrigatoriamente.

O resultado é retornado no formato JSON, informando o valor da predição e a versão do modelo.

json```
{
  "statusCode": 200,
  "prediction": 55198,
  "version": "linear_regression@v1.0.0
}
```