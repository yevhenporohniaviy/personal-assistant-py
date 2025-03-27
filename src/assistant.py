from src.address_book import AddressBook
from src.note_book import NoteBook
from src.record import Record, NoteRecord
from src.utils.input_parser import InputParser
from src.utils.localization import Localization

class Assistant:
    """Main assistant class that handles user interaction"""
    def __init__(self):
        self.address_book = AddressBook()
        self.note_book = NoteBook()
        self.running = False
        self.localization = Localization()
        
        # Define available commands
        self.commands = [
            "add contact", "show all", "search contacts", "edit contact", "delete contact", "birthdays",
            "add note", "search notes", "edit note", "delete note", "add tag", "search by tag", "sort by tags",
            "help", "exit", "quit", "q", "change language"
        ]
        
        # Initialize input parser
        self.input_parser = InputParser(self.commands)
    
    def run(self):
        """Run the main loop of the assistant"""
        self.running = True
        print(self.localization.get_text("welcome"))
        self.show_help()
        
        while self.running:
            try:
                user_input = input(self.localization.get_text("enter_command")).strip()
                self.process_command(user_input)
            except KeyboardInterrupt:
                print("\nGoodbye!")
                self.running = False
            except Exception as e:
                print(self.localization.get_text("error").format(str(e)))
    
    def process_command(self, user_input):
        """Process user command with intelligent parsing"""
        # Parse the input
        command, args = self.input_parser.parse_input(user_input)
        
        # Process the command
        if command in ["exit", "quit", "q"]:
            print(self.localization.get_text("goodbye"))
            self.running = False
        elif command == "help":
            self.show_help()
        # Contact commands
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
        # Note commands
        elif command == "add note":
            self.add_note()
        elif command == "search notes":
            self.search_notes()
        elif command == "edit note":
            self.edit_note()
        elif command == "delete note":
            self.delete_note()
        elif command == "add tag":
            self.add_tag_to_note()
        elif command == "search by tag":
            self.search_notes_by_tag()
        elif command == "sort by tags":
            self.sort_notes_by_tags()
        elif command == "change language":
            self.change_language()
        else:
            # Try to guess the command with improved algorithm
            guessed_commands = self.input_parser.guess_commands(user_input)
            
            if guessed_commands:
                if len(guessed_commands) == 1:
                    # Single suggestion
                    guessed_command = guessed_commands[0]
                    display_command = self.localization.get_text(guessed_command)
                    confirm_msg = self.localization.get_text("did_you_mean").format(display_command)
                    confirm = input(confirm_msg).strip().lower()
                    if confirm == 'y' or confirm == 'т': # 'т' is 'y' in Ukrainian
                        self.process_command(guessed_command)
                        return
                else:
                    # Multiple suggestions
                    print(self.localization.get_text("multiple_suggestions"))
                    for i, cmd in enumerate(guessed_commands, 1):
                        display_command = self.localization.get_text(cmd)
                        print(f"{i}. {display_command}")
                    
                    choice = input(self.localization.get_text("select_suggestion")).strip()
                    try:
                        idx = int(choice) - 1
                        if 0 <= idx < len(guessed_commands):
                            self.process_command(guessed_commands[idx])
                            return
                    except ValueError:
                        pass
            
            # Show context-sensitive help
            print(self.localization.get_text("command_not_recognized"))
            self.show_help(user_input)
    
    def show_help(self, context=None):
        """Show available commands with context-aware help"""
        print(f"\n{self.localization.get_text('available_commands')}")
        
        # Get commands and descriptions in current language
        commands = self.localization.get_command_dict()
        
        # Show context-specific help if context is provided
        if context:
            relevant_commands = [cmd for cmd in commands.items() if context.lower() in cmd[0].lower()]
            if relevant_commands:
                for cmd, desc in relevant_commands:
                    print(f"  {cmd}: {desc}")
                return
        
        # Show full help organized by category
        print("  Contact Management:")
        for cmd in ["add contact", "show all", "search contacts", "edit contact", "delete contact", "birthdays"]:
            desc_key = f"desc_{cmd.replace(' ', '_')}"
            display_cmd = self.localization.get_text(cmd)
            display_desc = self.localization.get_text(desc_key)
            print(f"  {display_cmd} - {display_desc}")
        
        print("\n  Note Management:")
        for cmd in ["add note", "search notes", "edit note", "delete note", "add tag", "search by tag", "sort by tags"]:
            desc_key = f"desc_{cmd.replace(' ', '_')}"
            display_cmd = self.localization.get_text(cmd)
            display_desc = self.localization.get_text(desc_key)
            print(f"  {display_cmd} - {display_desc}")
        
        print("\n  Other Commands:")
        for cmd in ["help", "exit", "change language"]:
            desc_key = f"desc_{cmd.replace(' ', '_')}"
            display_cmd = self.localization.get_text(cmd)
            display_desc = self.localization.get_text(desc_key)
            print(f"  {display_cmd} - {display_desc}")
        print()
    
    # Contact management methods
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
            
            # Add birthday
            birthday = input("Enter birthday (YYYY-MM-DD, leave empty to skip): ").strip()
            if birthday:
                try:
                    record.add_birthday(birthday)
                except ValueError as e:
                    print(f"Error: {e}")
            
            # Add address
            address = input("Enter address (leave empty to skip): ").strip()
            if address:
                record.add_address(address)
            
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
            print("No contacts found.")
            return
        
        print("\nFound contacts:")
        for record in results:
            print(record)
    
    def edit_contact(self):
        """Edit an existing contact"""
        name = input("Enter contact name to edit: ").strip()
        record = self.address_book.find(name)
        
        if not record:
            print(f"Contact '{name}' not found.")
            return
        
        print("\nCurrent contact information:")
        print(record)
        
        while True:
            print("\nWhat would you like to edit?")
            print("1. Phone numbers")
            print("2. Email")
            print("3. Birthday")
            print("4. Address")
            print("0. Done")
            
            choice = input("Enter your choice (0-4): ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                self._edit_phones(record)
            elif choice == "2":
                self._edit_email(record)
            elif choice == "3":
                self._edit_birthday(record)
            elif choice == "4":
                self._edit_address(record)
            else:
                print("Invalid choice.")
    
    def delete_contact(self):
        """Delete a contact"""
        name = input("Enter contact name to delete: ").strip()
        if not name:
            print("Name cannot be empty.")
            return
        
        if self.address_book.delete(name):
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")
    
    def show_upcoming_birthdays(self):
        """Show upcoming birthdays"""
        days = input("Enter number of days to look ahead (default 7): ").strip()
        days = int(days) if days.isdigit() else 7
        
        birthdays = self.address_book.get_upcoming_birthdays(days)
        if not birthdays:
            print(f"No birthdays in the next {days} days.")
            return
        
        print(f"\nUpcoming birthdays in the next {days} days:")
        for record in birthdays:
            print(f"{record.name}: {record.birthday}")
    
    # Note management methods
    def add_note(self):
        """Add a new note"""
        try:
            title = input("Enter note title: ").strip()
            if not title:
                print("Title cannot be empty.")
                return
            
            # Check if note already exists
            if self.note_book.find(title):
                print(f"Note with title '{title}' already exists.")
                return
            
            content = input("Enter note content: ").strip()
            if not content:
                print("Content cannot be empty.")
                return
            
            # Create a new note record
            from src.record import NoteRecord
            record = NoteRecord(title, content)
            
            # Add tags
            while True:
                tag = input("Enter tag (leave empty to finish): ").strip()
                if not tag:
                    break
                record.add_tag(tag)
            
            # Add the record to the note book
            self.note_book.add_record(record)
            print(f"Note '{title}' added successfully.")
            
        except ValueError as e:
            print(f"Error: {e}")
    
    def search_notes(self):
        """Search for notes"""
        query = input("Enter search query: ").strip()
        if not query:
            print("Search query cannot be empty.")
            return
        
        notes = self.note_book.search(query)
        if not notes:
            print("No notes found.")
            return
        
        print("\nFound notes:")
        for note in notes:
            print(note)
            print("-" * 30)
    
    def edit_note(self):
        """Edit a note"""
        title = input("Enter note title to edit: ").strip()
        note = self.note_book.find(title)
        
        if not note:
            print(f"Note '{title}' not found.")
            return
        
        print("\nCurrent note:")
        print(note)
        
        new_content = input("Enter new content (leave empty to keep current): ").strip()
        if new_content:
            note.edit_content(new_content)
            self.note_book.save()
            print("Note content updated successfully.")
            
        # Ask if user wants to edit tags
        edit_tags = input("Do you want to edit tags? (y/n): ").strip().lower()
        if edit_tags == 'y':
            self._edit_note_tags(note)
            self.note_book.save()
        
        print("Note updated successfully.")
    
    def delete_note(self):
        """Delete a note"""
        title = input("Enter note title to delete: ").strip()
        if not title:
            print("Title cannot be empty.")
            return
        
        if self.note_book.delete(title):
            print(f"Note '{title}' deleted successfully.")
        else:
            print(f"Note '{title}' not found.")
    
    def add_tag_to_note(self):
        """Add a tag to a note"""
        title = input("Enter note title: ").strip()
        note = self.note_book.find(title)
        
        if not note:
            print(f"Note '{title}' not found.")
            return
        
        tag = input("Enter tag to add: ").strip()
        if not tag:
            print("Tag cannot be empty.")
            return
        
        if note.add_tag(tag):
            self.note_book.save()
            print(f"Tag '{tag}' added to note '{title}'")
        else:
            print(f"Tag '{tag}' already exists in note '{title}'")
            
    def _edit_note_tags(self, note):
        """Helper method to edit note tags"""
        while True:
            print("\nCurrent tags:")
            if note.tags:
                for i, tag in enumerate(note.tags, 1):
                    print(f"{i}. {tag}")
            else:
                print("No tags")
            
            print("\nOptions:")
            print("1. Add new tag")
            print("2. Remove tag")
            print("0. Done")
            
            choice = input("Enter your choice (0-2): ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                tag = input("Enter new tag: ").strip()
                if tag:
                    if note.add_tag(tag):
                        print(f"Tag '{tag}' added.")
                    else:
                        print(f"Tag '{tag}' already exists.")
                else:
                    print("Tag cannot be empty.")
            elif choice == "2":
                if not note.tags:
                    print("No tags to remove.")
                    continue
                
                idx = input(f"Enter number to remove (1-{len(note.tags)}): ").strip()
                if not idx.isdigit() or not 1 <= int(idx) <= len(note.tags):
                    print("Invalid index.")
                    continue
                
                tag = note.tags[int(idx)-1].value
                if note.remove_tag(tag):
                    print(f"Tag '{tag}' removed.")
                else:
                    print(f"Failed to remove tag '{tag}'.")
            else:
                print("Invalid choice.")
    
    def search_notes_by_tag(self):
        """Search notes by tag"""
        tag = input("Enter tag to search for: ").strip()
        if not tag:
            print("Tag cannot be empty.")
            return
        
        notes = self.note_book.search_by_tag(tag)
        if not notes:
            print(f"No notes found with tag '{tag}'")
            return
        
        print(f"\nNotes with tag '{tag}':")
        for note in notes:
            print(note)
            print("-" * 30)
    
    def sort_notes_by_tags(self):
        """Sort and display notes by tags"""
        sorted_notes = self.note_book.sort_by_tags()
        if not sorted_notes:
            print("No notes found.")
            return
        
        print("\nNotes sorted by tags:")
        for tag, notes in sorted_notes.items():
            if tag == "no_tags":
                print("\nNotes without tags:")
            else:
                print(f"\nTag: #{tag}")
            
            for note in notes:
                print(note)
                print("-" * 30)
    
    # Helper methods for contact editing
    def _edit_phones(self, record):
        """Helper method to edit phone numbers"""
        while True:
            print("\nCurrent phone numbers:")
            for i, phone in enumerate(record.phones, 1):
                print(f"{i}. {phone}")
            
            print("\nOptions:")
            print("1. Add new phone")
            print("2. Edit existing phone")
            print("3. Delete phone")
            print("0. Done")
            
            choice = input("Enter your choice (0-3): ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                phone = input("Enter new phone number: ").strip()
                try:
                    record.add_phone(phone)
                    print("Phone number added.")
                except ValueError as e:
                    print(f"Error: {e}")
            elif choice == "2":
                if not record.phones:
                    print("No phone numbers to edit.")
                    continue
                
                idx = input("Enter number to edit (1-{}): ".format(len(record.phones))).strip()
                if not idx.isdigit() or not 1 <= int(idx) <= len(record.phones):
                    print("Invalid index.")
                    continue
                
                new_phone = input("Enter new phone number: ").strip()
                try:
                    record.edit_phone(int(idx)-1, new_phone)
                    print("Phone number updated.")
                except ValueError as e:
                    print(f"Error: {e}")
            elif choice == "3":
                if not record.phones:
                    print("No phone numbers to delete.")
                    continue
                
                idx = input("Enter number to delete (1-{}): ".format(len(record.phones))).strip()
                if not idx.isdigit() or not 1 <= int(idx) <= len(record.phones):
                    print("Invalid index.")
                    continue
                
                record.delete_phone(int(idx)-1)
                print("Phone number deleted.")
            else:
                print("Invalid choice.")
    
    def _edit_email(self, record):
        """Helper method to edit email"""
        print(f"Current email: {record.email if record.email else 'None'}")
        email = input("Enter new email (leave empty to remove): ").strip()
        
        try:
            if email:
                record.add_email(email)
                print("Email updated.")
            elif record.email:
                record.remove_email()
                print("Email removed.")
        except ValueError as e:
            print(f"Error: {e}")
    
    def _edit_birthday(self, record):
        """Helper method to edit birthday"""
        print(f"Current birthday: {record.birthday if record.birthday else 'None'}")
        birthday = input("Enter new birthday (YYYY-MM-DD, leave empty to remove): ").strip()
        
        try:
            if birthday:
                record.add_birthday(birthday)
                print("Birthday updated.")
            elif record.birthday:
                record.remove_birthday()
                print("Birthday removed.")
        except ValueError as e:
            print(f"Error: {e}")
    
    def _edit_address(self, record):
        """Helper method to edit address"""
        print(f"Current address: {record.address if record.address else 'None'}")
        address = input("Enter new address (leave empty to remove): ").strip()
        
        if address:
            record.add_address(address)
            print("Address updated.")
        elif record.address:
            record.remove_address()
            print("Address removed.")
            
    def change_language(self):
        """Change the interface language"""
        if self.localization.change_language():
            # Reinitialize the input parser to update command mappings
            self.input_parser = InputParser(self.commands)