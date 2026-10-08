
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

def show_treatments_by_reserve(result: list | dict) -> None:
    if isinstance(result, dict) and "error" in result:
        print(f"\nError: {result['error']}")
        return

    if not result:
        print("\nNo treatments found for this ranger.")
        return

    print("\n===== Treatments by Reserve =====")
    for treatment in result:
        print(f"Reserve: {treatment['reserve_name']}")
        print(f"Unique animals treated: {treatment['animals_count']}")
        print("-" * 30)
    print("!!!!! Done !!!!!\n")