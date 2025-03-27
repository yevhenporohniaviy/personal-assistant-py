import re

def validate_phone(phone):
    """
    Validates phone number format.
    Accepts formats: +380501234567, 380501234567, 0501234567
    """
    # Remove any spaces, dashes, or parentheses
    phone = re.sub(r'[\s\-\(\)]', '', phone)
    
    # Check if the phone number matches one of the valid formats
    if re.match(r'^\+?\d{10,12}$', phone):
        return True
    return False

def validate_email(email):
    """
    Validates email format using a regular expression.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    return False