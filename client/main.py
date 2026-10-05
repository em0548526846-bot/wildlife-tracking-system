from animal_search import choose_search_type,read_animal_id,read_collar_code
from http_client import request_last_reserve
from output import show_last_reserve

def main():
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

if __name__ == "__main__":
    main()
