from datetime import datetime
import re
from src.utils.validators import validate_phone, validate_email

class Field:
    """Base class for record fields"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    """Name field for a record"""
    def __init__(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        super().__init__(value)

class Phone(Field):
    """Phone field for a record"""
    def __init__(self, value):
        if not validate_phone(value):
            raise ValueError("Invalid phone number format")
        super().__init__(value)

class Email(Field):
    """Email field for a record"""
    def __init__(self, value):
        if not validate_email(value):
            raise ValueError("Invalid email format")
        super().__init__(value)

class Address(Field):
    """Address field for a record"""
    pass

class Birthday(Field):
    """Birthday field for a record"""
    def __init__(self, value):
        try:
            # Convert string to datetime object
            self.date = datetime.strptime(value, "%Y-%m-%d").date()
            super().__init__(value)
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")

class Tag(Field):
    """Tag field for a note"""
    def __init__(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Tag must be a non-empty string")
        # Remove # if present at the beginning
        if value.startswith('#'):
            value = value[1:]
        super().__init__(value)

    def __str__(self):
        return f"#{self.value}"