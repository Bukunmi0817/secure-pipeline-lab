import os
import subprocess # Use the more secure module

def welcome_user(name):
    print(f"Hello, {name}! Welcome to the Secure Pipeline Lab.")

def secure_ping():
    # SECURE VERSION: We split the command and the argument.
    # We also disable the shell so commands cannot be 'chained'.
    target = input("Enter an IP to ping: ")
    try:
        # shell=False is the hero here
        subprocess.run(["ping", "-c", "1", target], shell=False, check=True)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    user_name = "Security Student"
    welcome_user(user_name)
    
    app_credential = os.getenv("APP_AUTH")
    
    # Call the SECURE version now
    secure_ping()