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
        # Enhanced validation for phone number
        if not value.isdigit():
            raise ValueError("Phone number must contain only digits")
        if len(value) < 10:
            raise ValueError("Phone number must be at least 10 digits long")
        if len(value) > 15:
            raise ValueError("Phone number is too long (maximum 15 digits)")
        super().__init__(value)