from animal_search import choose_search_type, read_animal_id, read_collar_code
from http_client import request_last_reserve, register_user, register_treatment, treatments_by_reserve
from output import show_last_reserve, show_treatments_by_reserve
from treatments_search import read_ranger_id, read_treatment_data, read_user, read_ranger_name, search_type_treatments


def menu():
    print('===Menu===')
    print("1. Find the animal's last known location.")
    print('2. Find treatments by reserve')
    print('3. New User Registration')
    print("4. New Treatment Registration")
    print("5. Exit")


def last_reserve():
    search_type = choose_search_type()
    if search_type == 'id':
        animal_id = read_animal_id()
        result = request_last_reserve('id', animal_id)
    elif search_type == 'collar_code':
        collar_code = read_collar_code()
        result = request_last_reserve('collar_code', collar_code)
    else:
        print("Invalid search type")
        return
    show_last_reserve(result)


def treatments_by_reserve_menu():
    search_type = search_type_treatments()
    user = read_user()
    if search_type == 'id':
        ranger_id = read_ranger_id()
        result = treatments_by_reserve('id', ranger_id, user)
    elif search_type == 'name':
        ranger_name = read_ranger_name()
        result = treatments_by_reserve('name', ranger_name, user)
    else:
        print("Invalid search type")
        return
    show_treatments_by_reserve(result)


def new_user_registration():
    user = read_user()
    user_dict = {'username': user[0], 'password': user[1]}
    result = register_user(user_dict)
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(result.get("message", "Operation completed successfully"))


def new_treatment_registration():
    user = read_user()
    treatment_data = read_treatment_data()
    result = register_treatment(treatment_data, user)
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(result.get("message", "Operation completed successfully"))

def main():
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            last_reserve()
        elif choice == '2':
            treatments_by_reserve_menu()
        elif choice == '3':
            new_user_registration()
        elif choice == '4':
            new_treatment_registration()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
