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

class Email(Field):
    """Email field for a record"""
    def __init__(self, value):
        # Basic email validation
        if value and '@' not in value:
            raise ValueError("Invalid email format. Must contain '@' symbol")
        super().__init__(value)

class Address(Field):
    """Address field for a record"""
    def __init__(self, value):
        super().__init__(value)

class Birthday(Field):
    """Birthday field for a record"""
    import datetime
    
    def __init__(self, value):
        # Validate and convert birthday to datetime object
        if value:
            try:
                # Expected format: DD.MM.YYYY
                day, month, year = map(int, value.split('.'))
                birthday_date = self.datetime.date(year, month, day)
                
                # Check if date is not in the future
                if birthday_date > self.datetime.date.today():
                    raise ValueError("Birthday cannot be in the future")
                    
                super().__init__(value)
                self.date = birthday_date
            except ValueError as e:
                if str(e) == "Birthday cannot be in the future":
                    raise
                raise ValueError("Invalid date format. Use DD.MM.YYYY")
        else:
            super().__init__(value)
            self.date = None
    
    def __str__(self):
        return self.value if self.value else "Not specified"