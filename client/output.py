
def show_last_reserve(result: dict) -> None:
    if "error" in result:
        print(result["error"])
    else:
        print(f"""
        ===== Results =====
        Animal
        ID: {result['animal_id']}
        Collar code: {result['collar_code']}
        Species: {result['species']} ({result['nickname']})
        Last seen reserve: {result['reserve_name']}
        Region: {result['region']}
        Description: {result['description']}
        """)

