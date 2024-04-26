import re
"""
    Password must contain:
    - At least 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
"""

def main():
    username = input("Username: ")
    password = input("Password: ")

    result = bool(re.match(r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}",password))

    if result:
        print("Succesfully Registered")
    else:
        print("""
    Password must contain:
    - At least 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    """)
main()