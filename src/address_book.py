from collections import UserDict
import pickle
import os

class AddressBook(UserDict):
    """Class for storing and managing contacts"""
    
    def __init__(self, file_path="address_book.pickle"):
        super().__init__()
        self.file_path = file_path
        self.load_from_file()
    
    def add_record(self, record):
        """Add a new contact record to the address book"""
        self.data[record.name.value] = record
        self.save_to_file()
        return True
    
    def find(self, name):
        """Find a contact by name"""
        return self.data.get(name)
    
    def delete(self, name):
        """Delete a contact by name"""
        if name in self.data:
            del self.data[name]
            self.save_to_file()
            return True
        return False
    
    def search(self, query):
        """Search contacts by any field"""
        results = []
        query = query.lower()
        
        for record in self.data.values():
            # Search in name
            if query in record.name.value.lower():
                results.append(record)
                continue
                
            # Search in phones
            if any(query in phone.value.lower() for phone in record.phones):
                results.append(record)
                continue
                
            # Search in email
            if record.email and query in record.email.value.lower():
                results.append(record)
                continue
                
            # Search in address
            if record.address and query in record.address.value.lower():
                results.append(record)
                continue
                
            # Search in birthday
            if record.birthday and query in record.birthday.value.lower():
                results.append(record)
                continue
                
        return results
    
    def get_upcoming_birthdays(self, days=7):
        """Get contacts with birthdays in the next specified days"""
        upcoming_birthdays = []
        
        for record in self.data.values():
            if record.birthday and record.birthday.date:
                days_to_birthday = record.days_to_birthday()
                if days_to_birthday is not None and days_to_birthday <= days:
                    upcoming_birthdays.append((record, days_to_birthday))
        
        # Sort by days to birthday
        upcoming_birthdays.sort(key=lambda x: x[1])
        return upcoming_birthdays
    
    def save_to_file(self):
        """Save address book to file"""
        with open(self.file_path, 'wb') as file:
            pickle.dump(self.data, file)
    
    def load_from_file(self):
        """Load address book from file"""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'rb') as file:
                    self.data = pickle.load(file)
            except (pickle.UnpicklingError, EOFError):
                # If file is corrupted, start with empty address book
                self.data = {}
    
    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())