import csv
from pathlib import Path
import bcrypt
USERS_FILE = Path(__file__).parent / "users.csv"

def register_user(username: str, password: str):
    with open (USERS_FILE,mode='r',encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0]==username:
                raise ValueError('Username already exists')
    pass_hash=bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(12))
    decod=pass_hash.decode('utf-8')

    with open (USERS_FILE,mode='a',newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([username,decod])

def verify_user(username: str, password: str):
    with open (USERS_FILE,mode='r',encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            if row and row[0]==username:
                password_hash=row[1]
                return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))
    return False




