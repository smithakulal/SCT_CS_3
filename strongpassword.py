import re

def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r'[A-Z]', password):  
        strength += 1
    if re.search(r'[a-z]', password):  
        strength += 1
    if re.search(r'\d', password):     
        strength += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):  
        strength += 1

    if strength == 5:
        return "Strong"
    elif strength >= 3:
        return "Medium"
    else:
        return "Weak"

password = input("Enter a password: ")
print(f"Password Strength: {check_password_strength(password)}")
