import os

def welcome_user(name):
    print(f"Hello, {name}! Welcome to the Secure Pipeline Lab.")

if __name__ == "__main__":
    user_name = "Security Student"
    welcome_user(user_name)

    # REMEDIATION: We no longer hardcode the key. 
    # We tell the app to look for an environment variable instead.
    INTERNAL_API_KEY = os.getenv("MY_SECRET_API_KEY")
    
    if INTERNAL_API_KEY:
        print("API Key loaded securely.")
    else:
        print("No API Key found, but at least it's not leaked!")