from datetime import datetime

def read_non_empty(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        print("This field cannot be empty")

def read_positive_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive integer")
        except ValueError:
            print("Please enter a valid integer")

def read_date(prompt: str) -> str:
    while True:
        try:
            value = input(prompt).strip()
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("Please enter a valid date (YYYY-MM-DD)")

def read_outcome(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value in ['treated','relocated','healthy']:
            return value
        print("Please enter a valid outcome (treated, relocated, health)")


def read_user():
        username= read_non_empty("Enter username: ")
        password= read_non_empty("Enter password: ")
        return username, password

def read_treatment_data() -> dict:
    animal_id = read_positive_int("Enter animal ID: ")
    ranger_id = read_positive_int("Enter ranger ID: ")
    reserve_id = read_positive_int("Enter reserve ID: ")
    date = read_date("Enter date (YYYY-MM-DD): ")
    outcome = read_outcome("Enter outcome (treated, relocated, health): ")
    return {
        "animal_id": animal_id,
        "ranger_id": ranger_id,
        "reserve_id": reserve_id,
        "date": date,
        "outcome": outcome
    }
def search_type_treatments() -> str:
    while True:
        value = input("Enter search type (id, name): ").strip()
        if value in ['id', 'name']:
            return value
        print("Please enter a valid search type (id, name)")

def read_ranger_id() -> int:
    return read_positive_int("Enter ranger ID: ")

def read_ranger_name() -> str:
    return read_non_empty("Enter ranger name: ")
