from src.field import Name, Phone

class Record:
    """Class for storing contact information"""
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, phone):
        """Add a phone number to the contact"""
        self.phones.append(Phone(phone))
    
    def remove_phone(self, phone):
        """Remove a phone number from the contact"""
        for i, p in enumerate(self.phones):
            if p.value == phone:
                return self.phones.pop(i)
    
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
    
    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(str(p) for p in self.phones)}"