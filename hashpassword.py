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

def update_json(username, score, result):
    file_path = 'users.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            users = json.load(f)
        for user in users:
            if user['username'] == username:
                user.setdefault('score', 0)
                user.setdefault('wins', 0)
                user.setdefault('losses', 0)
                
                user['score'] = score
                if result == "win":
                    user['wins'] += 1
                elif result == "lose":
                    user['losses'] += 1  
                break
        with open(file_path, 'w') as f:
            json.dump(users, f, indent=4)

def update_game_result(username, score, result):
    file_path = 'users.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            users = json.load(f)
        for user in users:
            if user['username'] == username:
                user.setdefault('score', 0)
                user.setdefault('wins', 0)
                user.setdefault('losses', 0)
                
                user['score'] = score  
                if result.lower() == "win":
                    user['wins'] += 1
                elif result.lower() == "lose":
                    user['losses'] += 1
                break
        with open(file_path, 'w') as f:
            json.dump(users, f, indent=4)
    else:
        print(f"Error: {file_path} not found!")