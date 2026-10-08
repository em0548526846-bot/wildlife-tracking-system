def choose_search_type() -> str:
    while True:
        choice = input("Choose search type (1 for animal ID, 2 for collar code): ").strip()
        if choice == "1":
            return "id"
        elif choice == "2":
            return "collar_code"
        else:
            print("Invalid choice. Please try again.")


def read_animal_id() -> int:
    while True:
        try:
            choice = int(input("Enter animal ID: "))
            if choice > 0:
                return choice
            else:
                print("Animal ID must be a positive integer. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def read_collar_code() -> str:
    while True:
        choice = input("Enter collar code: ").strip(  )
        if choice[0:4] == "COL-":
            return choice
        else:
            print("Collar code must start with 'COL-'. Please try again.")
