from src.field import Name, Phone, Email, Address, Birthday

class Record:
    """Class for storing contact information"""
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.email = None
        self.address = None
        self.birthday = None
    
    def add_phone(self, phone):
        """Add a phone number to the contact"""
        self.phones.append(Phone(phone))
    
    def remove_phone(self, phone):
        """Remove a phone number from the contact"""
        for i, p in enumerate(self.phones):
            if p.value == phone:
                return self.phones.pop(i)
        return None
    
    def edit_phone(self, old_phone, new_phone):
        """Edit a phone number"""
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return True
        return False
    
    def find_phone(self, phone):
        """Find a phone number"""
        for p in self.phones:
            if p.value == phone:
                return p
        return None
    
    def add_email(self, email):
        """Add or update email"""
        if email:
            self.email = Email(email)
            return True
        return False
    
    def add_address(self, address):
        """Add or update address"""
        if address:
            self.address = Address(address)
            return True
        return False
    
    def add_birthday(self, birthday):
        """Add or update birthday"""
        if birthday:
            self.birthday = Birthday(birthday)
            return True
        return False
    
    def days_to_birthday(self):
        """Calculate days to next birthday"""
        if not self.birthday or not self.birthday.date:
            return None
            
        import datetime
        today = datetime.date.today()
        next_birthday = datetime.date(today.year, self.birthday.date.month, self.birthday.date.day)
        
        # If the birthday has already occurred this year, calculate for next year
        if next_birthday < today:
            next_birthday = datetime.date(today.year + 1, self.birthday.date.month, self.birthday.date.day)
            
        return (next_birthday - today).days
    
    def __str__(self):
        result = f"Contact name: {self.name}"
        
        if self.phones:
            result += f", phones: {'; '.join(str(p) for p in self.phones)}"
        
        if self.email:
            result += f", email: {self.email}"
            
        if self.address:
            result += f", address: {self.address}"
            
        if self.birthday:
            result += f", birthday: {self.birthday}"
            days = self.days_to_birthday()
            if days is not None:
                result += f" (in {days} days)"
                
        return result