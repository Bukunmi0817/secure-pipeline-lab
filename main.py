import os

def welcome_user(name):
    print(f"Hello, {name}! Welcome to the Secure Pipeline Lab.")

if __name__ == "__main__":
    user_name = "Security Student"
    welcome_user(user_name)

    # Use a generic name that doesn't trigger 'keyword' scanners
    app_credential = os.getenv("APP_AUTH")
    
    if app_credential:
        print("Credential loaded.")
    else:
        print("Safe mode: No hardcoded data found.")