from datetime import datetime, timedelta
from src.field import Name, Phone, Email, Address, Birthday, Tag

class Record:
    """Base class for records in address book and note book"""
    def __init__(self, name):
        self.name = Name(name)
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return f"Record: {self.name}"

class ContactRecord(Record):
    """Class for contact records in address book"""
    def __init__(self, name):
        super().__init__(name)
        self.phones = []
        self.emails = []
        self.address = None
        self.birthday = None

    def add_phone(self, phone):
        """Add a phone number to the contact"""
        self.phones.append(Phone(phone))
        self.updated_at = datetime.now()

    def remove_phone(self, phone):
        """Remove a phone number from the contact"""
        for i, p in enumerate(self.phones):
            if p.value == phone:
                self.phones.pop(i)
                self.updated_at = datetime.now()
                return True
        return False

    def edit_phone(self, old_phone, new_phone):
        """Edit a phone number"""
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                self.updated_at = datetime.now()
                return True
        return False

    def add_email(self, email):
        """Add an email to the contact"""
        self.emails.append(Email(email))
        self.updated_at = datetime.now()

    def remove_email(self, email):
        """Remove an email from the contact"""
        for i, e in enumerate(self.emails):
            if e.value == email:
                self.emails.pop(i)
                self.updated_at = datetime.now()
                return True
        return False

    def edit_email(self, old_email, new_email):
        """Edit an email"""
        for i, e in enumerate(self.emails):
            if e.value == old_email:
                self.emails[i] = Email(new_email)
                self.updated_at = datetime.now()
                return True
        return False

    def set_address(self, address):
        """Set the address for the contact"""
        self.address = Address(address)
        self.updated_at = datetime.now()

    def set_birthday(self, birthday):
        """Set the birthday for the contact"""
        self.birthday = Birthday(birthday)
        self.updated_at = datetime.now()
        
    def edit_name(self, new_name):
        """Edit the name of the contact"""
        self.name = Name(new_name)
        self.updated_at = datetime.now()

    def days_to_birthday(self):
        """Calculate days to the next birthday"""
        if not self.birthday:
            return None

        today = datetime.now().date()
        birthday = self.birthday.date

        # Set the birthday for this year
        birthday_this_year = birthday.replace(year=today.year)

        # If the birthday has already occurred this year, calculate for next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Calculate the difference in days
        days_remaining = (birthday_this_year - today).days

        return days_remaining

    def __str__(self):
        result = [f"Contact: {self.name}"]
        
        if self.phones:
            result.append("Phones:")
            for phone in self.phones:
                result.append(f"  {phone}")
        
        if self.emails:
            result.append("Emails:")
            for email in self.emails:
                result.append(f"  {email}")
        
        if self.address:
            result.append(f"Address: {self.address}")
        
        if self.birthday:
            result.append(f"Birthday: {self.birthday}")
            days = self.days_to_birthday()
            if days is not None:
                result.append(f"Days to birthday: {days}")
        
        return "\n".join(result)

class NoteRecord(Record):
    """Class for note records in note book"""
    def __init__(self, name, content=""):
        super().__init__(name)
        self.content = content
        self.tags = []

    def add_tag(self, tag):
        """Add a tag to the note"""
        # Check if tag already exists
        for existing_tag in self.tags:
            if existing_tag.value.lower() == tag.lower():
                return False
        
        self.tags.append(Tag(tag))
        self.updated_at = datetime.now()
        return True

    def remove_tag(self, tag):
        """Remove a tag from the note"""
        # Remove # if present at the beginning
        if tag.startswith('#'):
            tag = tag[1:]
            
        for i, t in enumerate(self.tags):
            if t.value.lower() == tag.lower():
                self.tags.pop(i)
                self.updated_at = datetime.now()
                return True
        return False

    def edit_content(self, new_content):
        """Edit the content of the note"""
        self.content = new_content
        self.updated_at = datetime.now()

    def __str__(self):
        result = [f"Note: {self.name}"]
        
        if self.content:
            result.append(f"Content: {self.content}")
        
        if self.tags:
            result.append("Tags:")
            for tag in self.tags:
                result.append(f"  {tag}")
        
        result.append(f"Created: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        result.append(f"Updated: {self.updated_at.strftime('%Y-%m-%d %H:%M:%S')}")
        
        return "\n".join(result)