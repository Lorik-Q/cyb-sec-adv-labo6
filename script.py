# Onveilig gebruik van een hard-coded wachtwoord
def connect_to_database():
    password = "P@ssw0rd123"  # Dit zal een secret-scanning tool triggeren
    print("Connecting to database with password:", password)

# Gebruik van een kwetsbare versie van een dependency
try:
    import requests  # Zorg ervoor dat je een kwetsbare versie gebruikt in requirements.txt
    response = requests.get("https://example.com")
    print("Response status code:", response.status_code)
except ImportError:
    print("The requests library is not installed!")

# Onveilige code die een SAST-check kan triggeren
def eval_user_input():
    user_input = input("Enter something to evaluate: ")
    result = eval(user_input)  # Gebruik van eval() is een bekende kwetsbaarheid
    print("Result of evaluation:", result)

# Veilige code voor vergelijking
def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    connect_to_database()
    eval_user_input()
    print("Addition result:", add_numbers(2, 3))
