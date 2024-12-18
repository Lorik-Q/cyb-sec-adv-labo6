import sqlite3

# Kwetsbare SQL-query
def login(username, password):
    conn = sqlite3.connect("users.db")
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    conn.execute(query)
    conn.close()

# Hardcoded geheim
API_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

# Onveilige eval
def unsafe_eval():
    user_input = "print('Hacked!')"
    eval(user_input)

# Verouderde dependency in requirements.txt:
# flask==0.12
