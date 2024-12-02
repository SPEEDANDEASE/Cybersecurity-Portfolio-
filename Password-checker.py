import re

def check_password(password):
    # Check length
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    
    # Check for uppercase letter
    if not re.search("[A-Z]", password):
        return "Password must contain at least one uppercase letter."
    
    # Check for lowercase letter
    if not re.search("[a-z]", password):
        return "Password must contain at least one lowercase letter."
    
    # Check for a number
    if not re.search("[0-9]", password):
        return "Password must contain at least one number."
    
    # Check for special characters
    if not re.search("[@#$%^&+=]", password):
        return "Password must contain at least one special character (@, #, $, %, ^, &, +, =)."
    
    # If all checks pass
    return "Password is strong."

# Example usage
password = input("Enter password to check: ")
print(check_password(password))