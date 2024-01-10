from pathlib import Path
import src.app as app

def test_model_exists():
    arquivo_path = Path("model.pkl")
    assert arquivo_path.is_file()

def test_model_version_exists():
    arquivo_path = Path("model_version.txt")
    assert arquivo_path.is_file()

def test_handler_call():
    payload = {
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

    event = {"data": payload}
    result = app.handler(event, None)

    assert isinstance(result["prediction"], int)
    assert result["prediction"] >= 0
    assert result["statusCode"] == 200