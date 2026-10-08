from json import JSONDecodeError
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


def register_user(user_data: dict) -> dict:
    endpoint_url = f"{url}/users/register"
    response = requests.post(endpoint_url, json=user_data)
    try:
        data = response.json()
    except JSONDecodeError:
        data = {"error": response.text}
    if response.status_code == 201:
        return data
    error_message = data.get("detail", response.text) if isinstance(data, dict) else response.text
    return {"error": error_message}


def register_treatment(treatment_data: dict, user: tuple[str, str]) -> dict:
    endpoint_url = f"{url}/treatments"
    username, password = user
    headers = {
        "X-Username": username,
        "X-Password": password
    }
    response = requests.post(endpoint_url, json=treatment_data, headers=headers)
    try:
        data = response.json()
    except JSONDecodeError:
        data = {"error": response.text}

    if response.status_code == 201:
        return data

    error_message = data.get("detail", response.text) if isinstance(data, dict) else response.text
    return {"error": error_message}

def treatments_by_reserve(search_type,search_value,user: tuple[str, str]) -> list|dict:
    endpoint_url = f"{url}/rangers/treatments-by-reserve"
    username, password = user
    headers = {
        "X-Username": username,
        "X-Password": password
    }
    param_key = "ranger_id" if search_type == "id" else "ranger_name"
    params = {param_key: search_value}
    response = requests.get(endpoint_url, headers=headers, params=params)
    try:
        data = response.json()
    except JSONDecodeError:
        data = {"error": response.text}
    if response.status_code == 200:
        return data
    error_message = data.get("detail", response.text) if isinstance(data, dict) else response.text
    return {"error": error_message}

