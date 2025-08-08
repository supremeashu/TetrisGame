import json
import os

USERS_FILE = "users.json"

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, 'r') as file:
        return json.load(file)

def save_users(users):
    with open(USERS_FILE, 'w') as file:
        json.dump(users, file, indent=2)

def login_user():
    users = load_users()
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    if username in users:
        if users[username]['password'] == password:
            print("✅ Login successful.")
            return username, users[username]
        else:
            print("❌ Incorrect password.")
            exit()
    else:
        print("🆕 New user created.")
        users[username] = {
            "password": password,
            "level": 1,
            "score": 0,
            "lines": 0
        }
        save_users(users)
        return username, users[username]

def save_user_progress(username, level, score, lines):
    users = load_users()
    if username in users:
        users[username]["level"] = level
        users[username]["score"] = score
        users[username]["lines"] = lines
        save_users(users)

def login_user_by_input(username, password):
    users = load_users()

    if username in users:
        if users[username]['password'] == password:
            print("✅ Login successful.")
            return username, users[username]
        else:
            print("❌ Incorrect password.")
            exit()
    else:
        print("🆕 New user created.")
        users[username] = {
            "password": password,
            "level": 1,
            "score": 0,
            "lines": 0
        }
        save_users(users)
        return username, users[username]
