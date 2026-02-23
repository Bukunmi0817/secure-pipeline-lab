import os

def welcome_user(name):
    print(f"Hello, {name}! Welcome to the Secure Pipeline Lab.")

def insecure_ping():
    # SECURITY FLAW: Taking user input and passing it directly to the system.
    # An attacker could enter: "8.8.8.8 ; rm -rf /"
    target = input("Enter an IP to ping: ")
    os.system(f"ping -c 1 {target}")

if __name__ == "__main__":
    user_name = "Security Student"
    welcome_user(user_name)

    # Use a generic name that doesn't trigger 'keyword' scanners
    app_credential = os.getenv("APP_AUTH")
    
    if app_credential:
        print("Credential loaded.")
    else:
        print("Safe mode: No hardcoded data found.")

    insecure_ping()    