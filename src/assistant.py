from src.address_book import AddressBook
from src.note_book import NoteBook
from src.record import ContactRecord, NoteRecord
from src.utils.input_parser import InputParser
from src.utils.localization import Localization
from src.utils.rich_formatter import RichFormatter
from rich import box
from rich.table import Table

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
        
        # Welcome message with Rich formatting
        RichFormatter.print_header(self.localization.get_text("welcome"))
        self.show_help()
        
        while self.running:
            try:
                user_input = RichFormatter.ask_input(f"\n{self.localization.get_text('enter_command')}")
                self.process_command(user_input.strip())
            except KeyboardInterrupt:
                RichFormatter.print_warning("\nGoodbye!")
                self.running = False
            except Exception as e:
                RichFormatter.print_error(self.localization.get_text("error").format(str(e)))
    
    def process_command(self, user_input):
        """Process user command with intelligent parsing"""
        # Parse the input
        command, args = self.input_parser.parse_input(user_input)
        
        # Process the command
        if command in ["exit", "quit", "q"]:
            RichFormatter.print_info(self.localization.get_text("goodbye"))
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
                    confirm = RichFormatter.ask_confirm(confirm_msg, False)
                    if confirm:
                        self.process_command(guessed_command)
                        return
                else:
                    # Multiple suggestions
                    RichFormatter.print_warning(self.localization.get_text("multiple_suggestions"))
                    for i, cmd in enumerate(guessed_commands, 1):
                        display_command = self.localization.get_text(cmd)
                        RichFormatter.print_info(f"{i}. {display_command}")
                    
                    choice = RichFormatter.ask_input(self.localization.get_text("select_suggestion"))
                    try:
                        idx = int(choice) - 1
                        if 0 <= idx < len(guessed_commands):
                            self.process_command(guessed_commands[idx])
                            return
                    except ValueError:
                        pass
            
            # Show context-sensitive help
            RichFormatter.print_error(self.localization.get_text("command_not_recognized"))
            self.show_help(user_input)
    
    def show_help(self, context=None):
        """Show available commands with context-aware help"""
        RichFormatter.print_header(self.localization.get_text('available_commands'))
        
        # Get commands and descriptions in current language
        commands = self.localization.get_command_dict()
        
        # Show context-specific help if context is provided
        if context:
            relevant_commands = [cmd for cmd in commands.items() if context.lower() in cmd[0].lower()]
            if relevant_commands:
                for cmd, desc in relevant_commands:
                    RichFormatter.print_info(f"  {cmd}: {desc}")
                return
        
        # Create tables for each command category
        contact_table = Table(title="Contact Management", box=box.ROUNDED, expand=False)
        contact_table.add_column("Command", style="cyan")
        contact_table.add_column("Description", style="white")
        
        for cmd in ["add contact", "show all", "search contacts", "edit contact", "delete contact", "birthdays"]:
            desc_key = f"desc_{cmd.replace(' ', '_')}"
            display_cmd = self.localization.get_text(cmd)
            display_desc = self.localization.get_text(desc_key)
            contact_table.add_row(display_cmd, display_desc)
        
        note_table = Table(title="Note Management", box=box.ROUNDED, expand=False)
        note_table.add_column("Command", style="magenta")
        note_table.add_column("Description", style="white")
        
        for cmd in ["add note", "search notes", "edit note", "delete note", "add tag", "search by tag", "sort by tags"]:
            desc_key = f"desc_{cmd.replace(' ', '_')}"
            display_cmd = self.localization.get_text(cmd)
            display_desc = self.localization.get_text(desc_key)
            note_table.add_row(display_cmd, display_desc)
        
        other_table = Table(title="Other Commands", box=box.ROUNDED, expand=False)
        other_table.add_column("Command", style="green")
        other_table.add_column("Description", style="white")
        
        for cmd in ["help", "exit", "change language"]:
            desc_key = f"desc_{cmd.replace(' ', '_')}"
            display_cmd = self.localization.get_text(cmd)
            display_desc = self.localization.get_text(desc_key)
            other_table.add_row(display_cmd, display_desc)
        
        # Print the tables
        RichFormatter.console.print(contact_table)
        RichFormatter.console.print(note_table)
        RichFormatter.console.print(other_table)
    
    # Contact management methods
    def add_contact(self):
        """Add a new contact"""
        try:
            name = RichFormatter.ask_input("Enter name: ")
            if not name:
                RichFormatter.print_error("Name cannot be empty.")
                return
            
            # Check if contact already exists
            if self.address_book.find(name):
                RichFormatter.print_error(f"Contact '{name}' already exists.")
                return
            
            # Create a new contact record
            record = ContactRecord(name)
            
            # Add phone numbers
            while True:
                phone = RichFormatter.ask_input("Enter phone number (leave empty to skip): ")
                if not phone:
                    break
                try:
                    record.add_phone(phone)
                    add_another = RichFormatter.ask_confirm("Add another phone?", False)
                    if not add_another:
                        break
                except ValueError as e:
                    RichFormatter.print_error(f"Error: {e}")
            
            # Add email
            email = RichFormatter.ask_input("Enter email (leave empty to skip): ")
            if email:
                try:
                    record.add_email(email)
                except ValueError as e:
                    RichFormatter.print_error(f"Error: {e}")
            
            # Add birthday
            birthday = RichFormatter.ask_input("Enter birthday (YYYY-MM-DD, leave empty to skip): ")
            if birthday:
                try:
                    record.set_birthday(birthday)
                except ValueError as e:
                    RichFormatter.print_error(f"Error: {e}")
            
            # Add address
            address = RichFormatter.ask_input("Enter address (leave empty to skip): ")
            if address:
                record.set_address(address)
            
            # Add to address book
            self.address_book.add_record(record)
            RichFormatter.print_success(f"Contact '{name}' added successfully!")
            RichFormatter.display_contact(record)
            
        except Exception as e:
            RichFormatter.print_error(f"Error adding contact: {e}")
    
    def show_all_contacts(self):
        """Show all contacts"""
        if not self.address_book.data:
            RichFormatter.print_warning("Address book is empty.")
            return
        
        # Use rich formatter to display contacts
        RichFormatter.display_contacts_table(self.address_book.data.values())
    
    def search_contacts(self):
        """Search contacts"""
        query = RichFormatter.ask_input("Enter search query: ")
        if not query:
            RichFormatter.print_error("Search query cannot be empty.")
            return
        
        results = self.address_book.search(query)
        if not results:
            RichFormatter.print_warning(f"No contacts found for query '{query}'.")
            return
        
        RichFormatter.print_success(f"Found {len(results)} contacts:")
        RichFormatter.display_contacts_table(results)
    
    def edit_contact(self):
        """Edit a contact"""
        name = RichFormatter.ask_input("Enter contact name to edit: ")
        if not name:
            RichFormatter.print_error("Contact name cannot be empty.")
            return
        
        record = self.address_book.find(name)
        if not record:
            RichFormatter.print_error(f"Contact '{name}' not found.")
            return
        
        # Display the contact
        RichFormatter.display_contact(record)
        
        # Choose what to edit
        options = ["name", "phones", "email", "birthday", "address"]
        edit_table = Table(title="Edit Options", box=box.ROUNDED)
        edit_table.add_column("Option", style="cyan")
        edit_table.add_column("Description", style="white")
        
        edit_table.add_row("1", "Edit name")
        edit_table.add_row("2", "Edit phones")
        edit_table.add_row("3", "Edit email")
        edit_table.add_row("4", "Edit birthday")
        edit_table.add_row("5", "Edit address")
        
        RichFormatter.console.print(edit_table)
        
        choice = RichFormatter.ask_input("Choose what to edit (1-5): ")
        
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                field = options[idx]
                if field == "name":
                    new_name = RichFormatter.ask_input("Enter new name: ")
                    if new_name and new_name != name:
                        # Check if the new name already exists
                        if self.address_book.find(new_name):
                            RichFormatter.print_error(f"Contact '{new_name}' already exists.")
                            return
                        old_name = record.name.value
                        record.edit_name(new_name)
                        # Update the key in the address book
                        self.address_book.data[new_name] = record
                        del self.address_book.data[old_name]
                        self.address_book.save()
                        RichFormatter.print_success(f"Name updated from '{old_name}' to '{new_name}'.")
                elif field == "phones":
                    self._edit_phones(record)
                elif field == "email":
                    self._edit_email(record)
                elif field == "birthday":
                    self._edit_birthday(record)
                elif field == "address":
                    self._edit_address(record)
                
                # Display updated contact
                RichFormatter.print_success("Contact updated successfully!")
                RichFormatter.display_contact(record)
        except ValueError:
            RichFormatter.print_error("Invalid choice.")
    
    def delete_contact(self):
        """Delete a contact"""
        name = RichFormatter.ask_input("Enter contact name to delete: ")
        if not name:
            RichFormatter.print_error("Contact name cannot be empty.")
            return
        
        record = self.address_book.find(name)
        if not record:
            RichFormatter.print_error(f"Contact '{name}' not found.")
            return
        
        # Display the contact and confirm deletion
        RichFormatter.display_contact(record)
        confirm = RichFormatter.ask_confirm(f"Are you sure you want to delete contact '{name}'?", False)
        
        if confirm:
            self.address_book.delete(name)
            RichFormatter.print_success(f"Contact '{name}' deleted successfully.")
        else:
            RichFormatter.print_info("Deletion cancelled.")
    
    def show_upcoming_birthdays(self):
        """Show upcoming birthdays"""
        try:
            days = int(RichFormatter.ask_input("Enter number of days to check: ", "7"))
            if days < 0:
                RichFormatter.print_error("Number of days should be positive.")
                return
        except ValueError:
            RichFormatter.print_error("Please enter a valid number.")
            return
        
        upcoming = self.address_book.get_birthdays(days)
        if not upcoming:
            RichFormatter.print_warning(f"No birthdays in the next {days} days.")
            return
        
        # Create a table for birthdays
        birthday_table = Table(title=f"Upcoming Birthdays (Next {days} days)", box=box.ROUNDED)
        birthday_table.add_column("Name", style="cyan")
        birthday_table.add_column("Birthday", style="green")
        birthday_table.add_column("Days Left", style="magenta")
        
        for record, days_left in upcoming:
            birthday_display = record.birthday.value
            days_text = "Today!" if days_left == 0 else f"{days_left} days"
            birthday_table.add_row(record.name.value, birthday_display, days_text)
        
        RichFormatter.console.print(birthday_table)
    
    # Note management methods
    def add_note(self):
        """Add a new note"""
        try:
            title = RichFormatter.ask_input("Enter note title: ")
            if not title:
                RichFormatter.print_error("Title cannot be empty.")
                return
            
            # Check if note already exists
            if self.note_book.find(title):
                RichFormatter.print_error(f"Note '{title}' already exists.")
                return
            
            # Get note content
            content = RichFormatter.ask_input("Enter note content: ")
            
            # Create a new note record
            note = NoteRecord(title, content)
            
            # Add tags
            if RichFormatter.ask_confirm("Do you want to add tags to this note?", False):
                self._edit_note_tags(note)
            
            # Add to note book
            self.note_book.add_record(note)
            RichFormatter.print_success(f"Note '{title}' added successfully!")
            RichFormatter.display_note(note)
            
        except Exception as e:
            RichFormatter.print_error(f"Error adding note: {e}")
    
    def search_notes(self):
        """Search notes by content"""
        query = RichFormatter.ask_input("Enter search query: ")
        if not query:
            RichFormatter.print_error("Search query cannot be empty.")
            return
        
        results = self.note_book.search(query)
        if not results:
            RichFormatter.print_warning(f"No notes found for query '{query}'.")
            return
        
        RichFormatter.print_success(f"Found {len(results)} notes:")
        RichFormatter.display_notes_table(results)
    
    def edit_note(self):
        """Edit a note"""
        title = RichFormatter.ask_input("Enter note title to edit: ")
        if not title:
            RichFormatter.print_error("Note title cannot be empty.")
            return
        
        note = self.note_book.find(title)
        if not note:
            RichFormatter.print_error(f"Note '{title}' not found.")
            return
        
        # Display the note
        RichFormatter.display_note(note)
        
        # Choose what to edit
        options = ["title", "content", "tags"]
        edit_table = Table(title="Edit Options", box=box.ROUNDED)
        edit_table.add_column("Option", style="cyan")
        edit_table.add_column("Description", style="white")
        
        edit_table.add_row("1", "Edit title")
        edit_table.add_row("2", "Edit content")
        edit_table.add_row("3", "Edit tags")
        
        RichFormatter.console.print(edit_table)
        
        choice = RichFormatter.ask_input("Choose what to edit (1-3): ")
        
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                field = options[idx]
                if field == "title":
                    new_title = RichFormatter.ask_input("Enter new title: ")
                    if new_title and new_title != title:
                        # Check if the new title already exists
                        if self.note_book.find(new_title):
                            RichFormatter.print_error(f"Note '{new_title}' already exists.")
                            return
                        old_title = note.name.value
                        note.edit_name(new_title)
                        # Update the key in the note book
                        self.note_book.data[new_title] = note
                        del self.note_book.data[old_title]
                        self.note_book.save()
                        RichFormatter.print_success(f"Title updated from '{old_title}' to '{new_title}'.")
                elif field == "content":
                    current_content = note.content
                    RichFormatter.print_info(f"Current content: {current_content}")
                    new_content = RichFormatter.ask_input("Enter new content: ")
                    note.edit_content(new_content)
                    self.note_book.save()
                    RichFormatter.print_success("Content updated successfully.")
                elif field == "tags":
                    self._edit_note_tags(note)
                
                # Display updated note
                RichFormatter.print_success("Note updated successfully!")
                RichFormatter.display_note(note)
        except ValueError:
            RichFormatter.print_error("Invalid choice.")
    
    def delete_note(self):
        """Delete a note"""
        title = RichFormatter.ask_input("Enter note title to delete: ")
        if not title:
            RichFormatter.print_error("Note title cannot be empty.")
            return
        
        note = self.note_book.find(title)
        if not note:
            RichFormatter.print_error(f"Note '{title}' not found.")
            return
        
        # Display the note and confirm deletion
        RichFormatter.display_note(note)
        confirm = RichFormatter.ask_confirm(f"Are you sure you want to delete note '{title}'?", False)
        
        if confirm:
            self.note_book.delete(title)
            RichFormatter.print_success(f"Note '{title}' deleted successfully.")
        else:
            RichFormatter.print_info("Deletion cancelled.")
    
    def add_tag_to_note(self):
        """Add a tag to an existing note"""
        title = RichFormatter.ask_input("Enter note title: ")
        if not title:
            RichFormatter.print_error("Note title cannot be empty.")
            return
        
        note = self.note_book.find(title)
        if not note:
            RichFormatter.print_error(f"Note '{title}' not found.")
            return
        
        RichFormatter.display_note(note)
        self._edit_note_tags(note)
    
    def _edit_note_tags(self, note):
        """Edit tags for a note"""
        while True:
            # Display current tags
            if note.tags:
                tag_text = " ".join([f"#{tag.value}" for tag in note.tags])
                RichFormatter.print_info(f"Current tags: {tag_text}")
            else:
                RichFormatter.print_info("No tags set.")
            
            # Options table
            tags_table = Table(title="Tag Options", box=box.ROUNDED)
            tags_table.add_column("Option", style="cyan")
            tags_table.add_column("Description", style="white")
            
            tags_table.add_row("1", "Add a tag")
            tags_table.add_row("2", "Remove a tag")
            tags_table.add_row("3", "Done editing tags")
            
            RichFormatter.console.print(tags_table)
            
            choice = RichFormatter.ask_input("Choose an option (1-3): ")
            
            if choice == "1":
                tag = RichFormatter.ask_input("Enter tag (without #): ")
                if not tag:
                    RichFormatter.print_error("Tag cannot be empty.")
                    continue
                
                # Remove # if present
                if tag.startswith('#'):
                    tag = tag[1:]
                
                if note.add_tag(tag):
                    self.note_book.save()
                    RichFormatter.print_success(f"Tag #{tag} added successfully.")
                else:
                    RichFormatter.print_warning(f"Tag #{tag} already exists for this note.")
            
            elif choice == "2":
                if not note.tags:
                    RichFormatter.print_warning("No tags to remove.")
                    continue
                
                # Display tags with indices
                for i, tag in enumerate(note.tags, 1):
                    RichFormatter.print_info(f"{i}. #{tag.value}")
                
                idx = RichFormatter.ask_input("Enter tag number to remove (or 0 to cancel): ")
                try:
                    idx = int(idx)
                    if idx == 0:
                        continue
                    if 1 <= idx <= len(note.tags):
                        tag_to_remove = note.tags[idx-1].value
                        if note.remove_tag(tag_to_remove):
                            self.note_book.save()
                            RichFormatter.print_success(f"Tag #{tag_to_remove} removed successfully.")
                        else:
                            RichFormatter.print_error(f"Failed to remove tag #{tag_to_remove}.")
                    else:
                        RichFormatter.print_error("Invalid tag number.")
                except ValueError:
                    RichFormatter.print_error("Please enter a valid number.")
            
            elif choice == "3":
                break
            
            else:
                RichFormatter.print_error("Invalid choice.")
    
    def search_notes_by_tag(self):
        """Search notes by tag"""
        tag = RichFormatter.ask_input("Enter tag to search for (with or without #): ")
        if not tag:
            RichFormatter.print_error("Tag cannot be empty.")
            return
        
        results = self.note_book.search_by_tag(tag)
        if not results:
            RichFormatter.print_warning(f"No notes found with tag #{tag.lstrip('#')}.")
            return
        
        RichFormatter.print_success(f"Found {len(results)} notes with tag #{tag.lstrip('#')}:")
        RichFormatter.display_notes_table(results)
    
    def sort_notes_by_tags(self):
        """Sort and display notes grouped by tags"""
        sorted_notes = self.note_book.sort_by_tags()
        
        if not sorted_notes:
            RichFormatter.print_warning("No notes found.")
            return
        
        RichFormatter.print_header("Notes Sorted by Tags")
        
        for tag, notes in sorted_notes.items():
            if tag == "no_tags":
                tag_display = "Notes without tags"
            else:
                tag_display = f"Tag: #{tag}"
            
            # Create a table for each tag group
            tag_table = Table(title=tag_display, box=box.ROUNDED)
            tag_table.add_column("Title", style="cyan")
            tag_table.add_column("Content Preview", style="white")
            
            for note in notes:
                content_preview = (note.content[:30] + "...") if len(note.content) > 30 else note.content
                tag_table.add_row(note.name.value, content_preview)
            
            RichFormatter.console.print(tag_table)
    
    # Helper methods for contact editing
    def _edit_phones(self, record):
        """Helper method to edit contact phones"""
        while True:
            # Display current phones
            if record.phones:
                RichFormatter.print_info("Current phone numbers:")
                for i, phone in enumerate(record.phones, 1):
                    RichFormatter.print_info(f"{i}. {phone.value}")
            else:
                RichFormatter.print_info("No phone numbers set.")
            
            # Create options table
            phone_table = Table(title="Phone Options", box=box.ROUNDED)
            phone_table.add_column("Option", style="cyan")
            phone_table.add_column("Description", style="white")
            
            phone_table.add_row("1", "Add a phone number")
            phone_table.add_row("2", "Edit a phone number")
            phone_table.add_row("3", "Remove a phone number")
            phone_table.add_row("4", "Done editing phones")
            
            RichFormatter.console.print(phone_table)
            
            choice = RichFormatter.ask_input("Choose an option (1-4): ")
            
            if choice == "1":
                phone = RichFormatter.ask_input("Enter new phone number: ")
                if not phone:
                    RichFormatter.print_error("Phone number cannot be empty.")
                    continue
                
                try:
                    record.add_phone(phone)
                    self.address_book.save()
                    RichFormatter.print_success(f"Phone number {phone} added successfully.")
                except ValueError as e:
                    RichFormatter.print_error(f"Error: {e}")
            
            elif choice == "2":
                if not record.phones:
                    RichFormatter.print_warning("No phone numbers to edit.")
                    continue
                
                idx = RichFormatter.ask_input("Enter phone number to edit (or 0 to cancel): ")
                try:
                    idx = int(idx)
                    if idx == 0:
                        continue
                    if 1 <= idx <= len(record.phones):
                        old_phone = record.phones[idx-1].value
                        new_phone = RichFormatter.ask_input(f"Enter new phone number to replace {old_phone}: ")
                        if not new_phone:
                            RichFormatter.print_error("Phone number cannot be empty.")
                            continue
                        
                        try:
                            if record.edit_phone(old_phone, new_phone):
                                self.address_book.save()
                                RichFormatter.print_success(f"Phone number updated from {old_phone} to {new_phone}.")
                            else:
                                RichFormatter.print_error(f"Failed to update phone number.")
                        except ValueError as e:
                            RichFormatter.print_error(f"Error: {e}")
                    else:
                        RichFormatter.print_error("Invalid phone number index.")
                except ValueError:
                    RichFormatter.print_error("Please enter a valid number.")
            
            elif choice == "3":
                if not record.phones:
                    RichFormatter.print_warning("No phone numbers to remove.")
                    continue
                
                idx = RichFormatter.ask_input("Enter phone number to remove (or 0 to cancel): ")
                try:
                    idx = int(idx)
                    if idx == 0:
                        continue
                    if 1 <= idx <= len(record.phones):
                        phone = record.phones[idx-1].value
                        if record.remove_phone(phone):
                            self.address_book.save()
                            RichFormatter.print_success(f"Phone number {phone} removed successfully.")
                        else:
                            RichFormatter.print_error(f"Failed to remove phone number {phone}.")
                    else:
                        RichFormatter.print_error("Invalid phone number index.")
                except ValueError:
                    RichFormatter.print_error("Please enter a valid number.")
            
            elif choice == "4":
                break
            
            else:
                RichFormatter.print_error("Invalid choice.")
    
    def _edit_email(self, record):
        """Helper method to edit contact email"""
        if record.emails:
            RichFormatter.print_info("Current emails:")
            for i, email in enumerate(record.emails, 1):
                RichFormatter.print_info(f"{i}. {email.value}")
            
            # Choose to edit or remove or add new
            email_table = Table(title="Email Options", box=box.ROUNDED)
            email_table.add_column("Option", style="cyan")
            email_table.add_column("Description", style="white")
            
            email_table.add_row("1", "Edit an email")
            email_table.add_row("2", "Remove an email")
            email_table.add_row("3", "Add a new email")
            
            RichFormatter.console.print(email_table)
            
            choice = RichFormatter.ask_input("Choose an option (1-3): ")
            
            if choice == "1":
                idx = RichFormatter.ask_input("Enter email number to edit: ")
                try:
                    idx = int(idx)
                    if 1 <= idx <= len(record.emails):
                        old_email = record.emails[idx-1].value
                        new_email = RichFormatter.ask_input(f"Enter new email to replace {old_email}: ")
                        try:
                            if record.edit_email(old_email, new_email):
                                self.address_book.save()
                                RichFormatter.print_success(f"Email updated from {old_email} to {new_email}.")
                            else:
                                RichFormatter.print_error("Failed to update email.")
                        except ValueError as e:
                            RichFormatter.print_error(f"Error: {e}")
                    else:
                        RichFormatter.print_error("Invalid email index.")
                except ValueError:
                    RichFormatter.print_error("Please enter a valid number.")
            
            elif choice == "2":
                idx = RichFormatter.ask_input("Enter email number to remove: ")
                try:
                    idx = int(idx)
                    if 1 <= idx <= len(record.emails):
                        email = record.emails[idx-1].value
                        if record.remove_email(email):
                            self.address_book.save()
                            RichFormatter.print_success(f"Email {email} removed successfully.")
                        else:
                            RichFormatter.print_error(f"Failed to remove email {email}.")
                    else:
                        RichFormatter.print_error("Invalid email index.")
                except ValueError:
                    RichFormatter.print_error("Please enter a valid number.")
            
            elif choice == "3":
                email = RichFormatter.ask_input("Enter new email: ")
                try:
                    record.add_email(email)
                    self.address_book.save()
                    RichFormatter.print_success(f"Email {email} added successfully.")
                except ValueError as e:
                    RichFormatter.print_error(f"Error: {e}")
            
            else:
                RichFormatter.print_error("Invalid choice.")
        
        else:
            # No emails, just add a new one
            email = RichFormatter.ask_input("No emails set. Enter email: ")
            try:
                record.add_email(email)
                self.address_book.save()
                RichFormatter.print_success(f"Email {email} added successfully.")
            except ValueError as e:
                RichFormatter.print_error(f"Error: {e}")
    
    def _edit_birthday(self, record):
        """Helper method to edit contact birthday"""
        if record.birthday:
            RichFormatter.print_info(f"Current birthday: {record.birthday.value}")
            
            # Ask to edit or remove
            choice = RichFormatter.ask_input("Do you want to (1) edit or (2) remove the birthday? Enter choice (1/2): ")
            
            if choice == "1":
                birthday = RichFormatter.ask_input("Enter new birthday (YYYY-MM-DD): ")
                try:
                    record.set_birthday(birthday)
                    self.address_book.save()
                    RichFormatter.print_success(f"Birthday updated to {birthday}.")
                except ValueError as e:
                    RichFormatter.print_error(f"Error: {e}")
            
            elif choice == "2":
                record.birthday = None
                self.address_book.save()
                RichFormatter.print_success("Birthday removed.")
            
            else:
                RichFormatter.print_error("Invalid choice.")
        
        else:
            # No birthday set, just add a new one
            birthday = RichFormatter.ask_input("No birthday set. Enter birthday (YYYY-MM-DD): ")
            try:
                record.set_birthday(birthday)
                self.address_book.save()
                RichFormatter.print_success(f"Birthday set to {birthday}.")
            except ValueError as e:
                RichFormatter.print_error(f"Error: {e}")
    
    def _edit_address(self, record):
        """Helper method to edit contact address"""
        if record.address:
            RichFormatter.print_info(f"Current address: {record.address.value}")
            
            # Ask to edit or remove
            choice = RichFormatter.ask_input("Do you want to (1) edit or (2) remove the address? Enter choice (1/2): ")
            
            if choice == "1":
                address = RichFormatter.ask_input("Enter new address: ")
                record.set_address(address)
                self.address_book.save()
                RichFormatter.print_success(f"Address updated to {address}.")
            
            elif choice == "2":
                record.address = None
                self.address_book.save()
                RichFormatter.print_success("Address removed.")
            
            else:
                RichFormatter.print_error("Invalid choice.")
        
        else:
            # No address set, just add a new one
            address = RichFormatter.ask_input("No address set. Enter address: ")
            record.set_address(address)
            self.address_book.save()
            RichFormatter.print_success(f"Address set to {address}.")
    
    def change_language(self):
        """Change the interface language"""
        # Get available languages
        available_languages = self.localization.get_available_languages()
        
        # Create a table for language options
        lang_table = Table(title="Available Languages", box=box.ROUNDED)
        lang_table.add_column("Option", style="cyan")
        lang_table.add_column("Language", style="white")
        
        for i, (code, name) in enumerate(available_languages.items(), 1):
            lang_table.add_row(str(i), name)
        
        RichFormatter.console.print(lang_table)
        
        choice = RichFormatter.ask_input(f"Choose language (1-{len(available_languages)}): ")
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(available_languages):
                language_code = list(available_languages.keys())[idx]
                self.localization.set_language(language_code)
                # Reinitialize the input parser to update command mappings
                self.input_parser = InputParser(self.commands)
                RichFormatter.print_success(f"Language changed to {available_languages[language_code]}.")
            else:
                RichFormatter.print_error("Invalid choice.")
        except ValueError:
            RichFormatter.print_error("Please enter a valid number.")