import requests
from config import url

def request_last_reserve(search_type: str, search_value) -> dict:
    current_url = url + "/animals/last-reserve"
    param_key = "animal_id" if search_type == "id" else "collar_code"
    params = {param_key: search_value}
    response = requests.get(current_url, params=params)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return {"error": "Animal not found"}
    else:
        return {"error": response.text}
