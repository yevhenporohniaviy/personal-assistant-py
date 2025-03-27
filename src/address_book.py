from collections import UserDict
from src.record import ContactRecord
from src.utils.storage import Storage
from datetime import datetime, timedelta

class AddressBook(UserDict):
    """Class for storing and managing contacts"""
    def __init__(self):
        super().__init__()
        self.storage = Storage("address_book.pickle")
        # Load data from storage if available
        data = self.storage.load()
        if data:
            self.data = data
    
    def add_record(self, record):
        """Add a new contact record to the address book"""
        self.data[record.name.value] = record
        self.save()
        return True
    
    def find(self, name):
        """Find a contact by name"""
        return self.data.get(name)
    
    def delete(self, name):
        """Delete a contact by name"""
        if name in self.data:
            del self.data[name]
            self.save()
            return True
        return False
    
    def search(self, query):
        """Search contacts by name, phone, email, or address"""
        query = query.lower()
        results = []
        
        for record in self.data.values():
            # Search in name
            if query in record.name.value.lower():
                results.append(record)
                continue
            
            # Search in phones
            for phone in record.phones:
                if query in phone.value:
                    results.append(record)
                    break
            else:
                # Search in emails
                for email in record.emails:
                    if query in email.value.lower():
                        results.append(record)
                        break
                else:
                    # Search in address
                    if record.address and query in record.address.value.lower():
                        results.append(record)
        
        return results
    
    def get_birthdays(self, days=7):
        """Get contacts with birthdays in the next N days"""
        today = datetime.now().date()
        upcoming_birthdays = []
        
        for record in self.data.values():
            if record.birthday:
                days_to_birthday = record.days_to_birthday()
                if days_to_birthday is not None and days_to_birthday <= days:
                    upcoming_birthdays.append((record, days_to_birthday))
        
        # Sort by days to birthday
        upcoming_birthdays.sort(key=lambda x: x[1])
        
        return upcoming_birthdays
    
    def save(self):
        """Save address book to storage"""
        return self.storage.save(self.data)
    
    def __str__(self):
        if not self.data:
            return "Address book is empty"
        
        result = ["Address Book:"]
        for record in self.data.values():
            result.append(str(record))
            result.append("-" * 30)
        
        return "\n".join(result)