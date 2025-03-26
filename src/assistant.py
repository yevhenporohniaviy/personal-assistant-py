from src.address_book import AddressBook
from src.record import Record

class Assistant:
    """Main assistant class that handles user interaction"""
    def __init__(self):
        self.address_book = AddressBook()
        self.running = False
    
    def run(self):
        """Run the main loop of the assistant"""
        self.running = True
        print("Welcome to the Personal Assistant!")
        self.show_help()
        
        while self.running:
            try:
                command = input("Enter a command: ").strip().lower()
                self.process_command(command)
            except KeyboardInterrupt:
                print("\nGoodbye!")
                self.running = False
            except Exception as e:
                print(f"Error: {e}")
    
    def process_command(self, command):
        """Process user command"""
        if command in ["exit", "quit", "q"]:
            print("Goodbye!")
            self.running = False
        elif command == "help":
            self.show_help()
        elif command == "add contact":
            self.add_contact()
        elif command == "show all":
            self.show_all_contacts()
        elif command == "search contacts":
            self.search_contacts()
        elif command == "edit contact":
            self.edit_contact()
        elif command == "delete contact":
            self.delete_contact()
        elif command == "birthdays":
            self.show_upcoming_birthdays()
        else:
            print("Unknown command. Type 'help' for available commands.")
    
    def show_help(self):
        """Show available commands"""
        print("\nAvailable commands:")
        print("  add contact - Add a new contact")
        print("  show all - Show all contacts")
        print("  search contacts - Search for contacts")
        print("  edit contact - Edit an existing contact")
        print("  delete contact - Delete a contact")
        print("  birthdays - Show upcoming birthdays")
        print("  help - Show this help message")
        print("  exit/quit/q - Exit the program\n")
    
    def add_contact(self):
        """Add a new contact"""
        try:
            name = input("Enter name: ").strip()
            if not name:
                print("Name cannot be empty.")
                return
            
            # Check if contact already exists
            if self.address_book.find(name):
                print(f"Contact '{name}' already exists.")
                return
            
            # Create a new contact record
            record = Record(name)
            
            # Add phone numbers
            while True:
                phone = input("Enter phone number (leave empty to skip): ").strip()
                if not phone:
                    break
                try:
                    record.add_phone(phone)
                    add_another = input("Add another phone? (y/n): ").strip().lower()
                    if add_another != 'y':
                        break
                except ValueError as e:
                    print(f"Error: {e}")
            
            # Add email
            email = input("Enter email (leave empty to skip): ").strip()
            if email:
                try:
                    record.add_email(email)
                except ValueError as e:
                    print(f"Error: {e}")
            
            # Add address
            address = input("Enter address (leave empty to skip): ").strip()
            if address:
                record.add_address(address)
            
            # Add birthday
            birthday = input("Enter birthday in DD.MM.YYYY format (leave empty to skip): ").strip()
            if birthday:
                try:
                    record.add_birthday(birthday)
                except ValueError as e:
                    print(f"Error: {e}")
            
            # Add the record to the address book
            self.address_book.add_record(record)
            print(f"Contact '{name}' added successfully.")
            
        except ValueError as e:
            print(f"Error: {e}")
    
    def show_all_contacts(self):
        """Show all contacts"""
        if not self.address_book.data:
            print("No contacts found.")
            return
        
        print("\nAll contacts:")
        for record in self.address_book.data.values():
            print(record)
    
    def search_contacts(self):
        """Search for contacts"""
        query = input("Enter search query: ").strip()
        if not query:
            print("Search query cannot be empty.")
            return
        
        results = self.address_book.search(query)
        
        if not results:
            print(f"No contacts found matching '{query}'.")
            return
        
        print(f"\nFound {len(results)} contacts matching '{query}':")
        for record in results:
            print(record)
    
    def edit_contact(self):
        """Edit an existing contact"""
        name = input("Enter the name of the contact to edit: ").strip()
        if not name:
            print("Name cannot be empty.")
            return
        
        record = self.address_book.find(name)
        if not record:
            print(f"Contact '{name}' not found.")
            return
        
        print(f"\nEditing contact: {record}")
        
        while True:
            print("\nWhat would you like to edit?")
            print("1. Phone numbers")
            print("2. Email")
            print("3. Address")
            print("4. Birthday")
            print("0. Done editing")
            
            choice = input("Enter your choice (0-4): ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                self._edit_phones(record)
            elif choice == "2":
                self._edit_email(record)
            elif choice == "3":
                self._edit_address(record)
            elif choice == "4":
                self._edit_birthday(record)
            else:
                print("Invalid choice. Please try again.")
        
        # Save changes
        self.address_book.save_to_file()
        print(f"Contact '{name}' updated successfully.")
    
    def _edit_phones(self, record):
        """Edit phone numbers for a contact"""
        while True:
            print("\nPhone numbers:")
            if not record.phones:
                print("No phone numbers.")
            else:
                for i, phone in enumerate(record.phones):
                    print(f"{i+1}. {phone}")
            
            print("\nWhat would you like to do?")
            print("1. Add a new phone")
            print("2. Edit an existing phone")
            print("3. Delete a phone")
            print("0. Back to main edit menu")
            
            choice = input("Enter your choice (0-3): ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                phone = input("Enter new phone number: ").strip()
                try:
                    record.add_phone(phone)
                    print(f"Phone number '{phone}' added.")
                except ValueError as e:
                    print(f"Error: {e}")
            elif choice == "2":
                if not record.phones:
                    print("No phone numbers to edit.")
                    continue
                
                idx = input(f"Enter the number of the phone to edit (1-{len(record.phones)}): ").strip()
                try:
                    idx = int(idx) - 1
                    if idx < 0 or idx >= len(record.phones):
                        print("Invalid index.")
                        continue
                    
                    old_phone = record.phones[idx].value
                    new_phone = input(f"Enter new phone number to replace {old_phone}: ").strip()
                    
                    if record.edit_phone(old_phone, new_phone):
                        print(f"Phone number updated from '{old_phone}' to '{new_phone}'.")
                    else:
                        print(f"Failed to update phone number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            elif choice == "3":
                if not record.phones:
                    print("No phone numbers to delete.")
                    continue
                
                idx = input(f"Enter the number of the phone to delete (1-{len(record.phones)}): ").strip()
                try:
                    idx = int(idx) - 1
                    if idx < 0 or idx >= len(record.phones):
                        print("Invalid index.")
                        continue
                    
                    phone = record.phones[idx].value
                    if record.remove_phone(phone):
                        print(f"Phone number '{phone}' deleted.")
                    else:
                        print(f"Failed to delete phone number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("Invalid choice. Please try again.")
    
    def _edit_email(self, record):
        """Edit email for a contact"""
        print(f"Current email: {record.email if record.email else 'Not set'}")
        
        choice = input("Do you want to (1) add/update or (2) remove email? (1/2/cancel): ").strip().lower()
        
        if choice == "1":
            email = input("Enter new email: ").strip()
            try:
                record.add_email(email)
                print(f"Email updated to '{email}'.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            record.email = None
            print("Email removed.")
        elif choice.lower() == "cancel":
            return
        else:
            print("Invalid choice.")
    
    def _edit_address(self, record):
        """Edit address for a contact"""
        print(f"Current address: {record.address if record.address else 'Not set'}")
        
        choice = input("Do you want to (1) add/update or (2) remove address? (1/2/cancel): ").strip().lower()
        
        if choice == "1":
            address = input("Enter new address: ").strip()
            record.add_address(address)
            print(f"Address updated to '{address}'.")
        elif choice == "2":
            record.address = None
            print("Address removed.")
        elif choice.lower() == "cancel":
            return
        else:
            print("Invalid choice.")
    
    def _edit_birthday(self, record):
        """Edit birthday for a contact"""
        print(f"Current birthday: {record.birthday if record.birthday else 'Not set'}")
        
        choice = input("Do you want to (1) add/update or (2) remove birthday? (1/2/cancel): ").strip().lower()
        
        if choice == "1":
            birthday = input("Enter new birthday (DD.MM.YYYY): ").strip()
            try:
                record.add_birthday(birthday)
                print(f"Birthday updated to '{birthday}'.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            record.birthday = None
            print("Birthday removed.")
        elif choice.lower() == "cancel":
            return
        else:
            print("Invalid choice.")
    
    def delete_contact(self):
        """Delete a contact"""
        name = input("Enter the name of the contact to delete: ").strip()
        if not name:
            print("Name cannot be empty.")
            return
        
        record = self.address_book.find(name)
        if not record:
            print(f"Contact '{name}' not found.")
            return
        
        print(f"\nContact to delete: {record}")
        confirm = input(f"Are you sure you want to delete contact '{name}'? (y/n): ").strip().lower()
        
        if confirm == 'y':
            if self.address_book.delete(name):
                print(f"Contact '{name}' deleted successfully.")
            else:
                print(f"Failed to delete contact '{name}'.")
        else:
            print("Deletion cancelled.")
    
    def show_upcoming_birthdays(self):
        """Show upcoming birthdays"""
        days = input("Enter number of days to check for upcoming birthdays (default 7): ").strip()
        
        try:
            days = int(days) if days else 7
            if days <= 0:
                print("Number of days must be positive.")
                return
        except ValueError:
            print("Invalid input. Using default value of 7 days.")
            days = 7
        
        upcoming = self.address_book.get_upcoming_birthdays(days)
        
        if not upcoming:
            print(f"No birthdays in the next {days} days.")
            return
        
        print(f"\nUpcoming birthdays in the next {days} days:")
        for record, days_left in upcoming:
            print(f"{record.name.value}: {record.birthday.value} (in {days_left} days)")
    
    def find_contact(self, name):
        """Find a contact by name"""
        record = self.address_book.find(name)
        if record:
            print(f"\nFound contact:")
            print(record)
        else:
            print(f"Contact '{name}' not found.")