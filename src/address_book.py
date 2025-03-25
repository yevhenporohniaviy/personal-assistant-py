from collections import UserDict

class AddressBook(UserDict):
    """Class for storing and managing contacts"""
    
    def add_record(self, record):
        """Add a new contact record to the address book"""
        self.data[record.name.value] = record
        return True
    
    def find(self, name):
        """Find a contact by name"""
        return self.data.get(name)
    
    def delete(self, name):
        """Delete a contact by name"""
        if name in self.data:
            del self.data[name]
            return True
        return False
    
    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())