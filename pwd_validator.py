def password_valid(password):
    
    # Checking the length
    if len(password) < 8:
        return False
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():  # Special character check
            has_special = True
            
    # Return true only if all conditions are met
    return has_upper and has_digit and has_special and has_lower

print(password_valid("Hello123!"))