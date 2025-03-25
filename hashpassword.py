import hashlib
import json
import os

def hash_password(password):
    return hashlib.sha256((password + "5gz").encode('utf-8')).hexdigest()

def check_password(username, password):
    file_path = 'users.json'
    hashed_input_password = hash_password(password)
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            users = json.load(f)
        for user in users:
            if user['username'] == username:
                if user['password'] == hashed_input_password:
                    return True
                else:
                    return False
        return "not_found"
    else:
        return "not_found"

def add_user(username, password):
    file_path = 'users.json'
    hashed_password = hash_password(password)
    new_user = {
        "username": username,
        "password": hashed_password,
        "score": 0,
        "wins": 0,
        "losses": 0
    }

    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            users = json.load(f)
    else:
        users = []
    
    for user in users:
        if user['username'] == username:
            return False
    
    users.append(new_user)
    with open(file_path, 'w') as f:
        json.dump(users, f, indent=4)
    return True