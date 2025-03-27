from src.utils.storage import Storage

class Localization:
    """
    Class for handling multilingual support.
    Provides translations for UI strings in different languages.
    """
    def __init__(self):
        """
        Initialize localization with available languages and load saved preference.
        """
        self.languages = {
            "en": "English",
            "uk": "Українська"
        }
        
        # Default language
        self.current_language = "en"
        
        # Load saved language preference
        self.storage = Storage("language_settings.pickle")
        saved_language = self.storage.load()
        if saved_language and saved_language in self.languages:
            self.current_language = saved_language
        
        # Initialize translations
        self._init_translations()
    
    def _init_translations(self):
        """
        Initialize translations for all supported languages.
        """
        self.translations = {
            "en": {
                # Command names
                "add contact": "add contact",
                "search contacts": "search contacts",
                "edit contact": "edit contact",
                "delete contact": "delete contact",
                "birthdays": "birthdays",
                "add note": "add note",
                "search notes": "search notes",
                "edit note": "edit note",
                "delete note": "delete note",
                "add tag": "add tag",
                "search by tag": "search by tag",
                "sort by tags": "sort by tags",
                "help": "help",
                "exit": "exit",
                "change language": "change language",
                
                # Command descriptions
                "desc_add_contact": "Add a new contact",
                "desc_search_contacts": "Search contacts",
                "desc_edit_contact": "Edit a contact",
                "desc_delete_contact": "Delete a contact",
                "desc_birthdays": "Show upcoming birthdays",
                "desc_add_note": "Add a new note",
                "desc_search_notes": "Search notes",
                "desc_edit_note": "Edit a note",
                "desc_delete_note": "Delete a note",
                "desc_add_tag": "Add a tag to a note",
                "desc_search_by_tag": "Search notes by tag",
                "desc_sort_by_tags": "Sort notes by tags",
                "desc_help": "Show available commands",
                "desc_exit": "Exit the program",
                "desc_change_language": "Change interface language",
                
                # UI strings
                "welcome": "Welcome to Personal Assistant!",
                "enter_command": "Enter a command: ",
                "exiting": "Exiting...",
                "error": "Error: {}",
                "command_not_recognized": "Command not recognized. Type 'help' to see available commands.",
                "command_not_implemented": "Command not implemented yet.",
                "available_commands": "Available commands:",
                "did_you_mean": "Did you mean '{}'? (y/n): ",
                "goodbye": "Goodbye! Have a nice day!",
                "language_changed": "Language changed to English.",
                "select_language": "Select language:\n1. English\n2. Українська\nEnter number: "
            },
            "uk": {
                # Command names
                "add contact": "додати контакт",
                "search contacts": "пошук контактів",
                "edit contact": "редагувати контакт",
                "delete contact": "видалити контакт",
                "birthdays": "дні народження",
                "add note": "додати нотатку",
                "search notes": "пошук нотаток",
                "edit note": "редагувати нотатку",
                "delete note": "видалити нотатку",
                "add tag": "додати тег",
                "search by tag": "пошук за тегом",
                "sort by tags": "сортувати за тегами",
                "help": "допомога",
                "exit": "вихід",
                "change language": "змінити мову",
                
                # Command descriptions
                "desc_add_contact": "Додати новий контакт",
                "desc_search_contacts": "Пошук контактів",
                "desc_edit_contact": "Редагувати контакт",
                "desc_delete_contact": "Видалити контакт",
                "desc_birthdays": "Показати найближчі дні народження",
                "desc_add_note": "Додати нову нотатку",
                "desc_search_notes": "Пошук нотаток",
                "desc_edit_note": "Редагувати нотатку",
                "desc_delete_note": "Видалити нотатку",
                "desc_add_tag": "Додати тег до нотатки",
                "desc_search_by_tag": "Пошук нотаток за тегом",
                "desc_sort_by_tags": "Сортувати нотатки за тегами",
                "desc_help": "Показати доступні команди",
                "desc_exit": "Вийти з програми",
                "desc_change_language": "Змінити мову інтерфейсу",
                
                # UI strings
                "welcome": "Ласкаво просимо до Персонального Помічника!",
                "enter_command": "Введіть команду: ",
                "exiting": "Виходимо...",
                "error": "Помилка: {}",
                "command_not_recognized": "Команда не розпізнана. Введіть 'допомога' для перегляду доступних команд.",
                "command_not_implemented": "Команда ще не реалізована.",
                "available_commands": "Доступні команди:",
                "did_you_mean": "Можливо, ви мали на увазі '{}'? (т/н): ",
                "goodbye": "До побачення! Гарного дня!",
                "language_changed": "Мову змінено на українську.",
                "select_language": "Виберіть мову:\n1. English\n2. Українська\nВведіть номер: "
            }
        }
    
    def get_text(self, key):
        """
        Get translated text for a key in the current language.
        """
        if key in self.translations[self.current_language]:
            return self.translations[self.current_language][key]
        return key
    
    def get_command_dict(self):
        """
        Get a dictionary of commands and their descriptions in the current language.
        """
        commands = {}
        for key, value in self.translations[self.current_language].items():
            if key.startswith("desc_"):
                # Get the command name from the description key
                cmd_key = key[5:]  # Remove 'desc_' prefix
                # Find the translated command name
                for cmd, cmd_trans in self.translations[self.current_language].items():
                    if cmd == cmd_key:
                        commands[cmd_trans] = value
                        break
        return commands
    
    def get_original_command(self, translated_command):
        """
        Get the original (English) command name from a translated command.
        """
        # Find the key in the current language that matches the translated command
        for key, value in self.translations[self.current_language].items():
            if value == translated_command and not key.startswith("desc_"):
                # Return the same key from the English translations
                return key
        return translated_command
    
    def change_language(self):
        """
        Change the current language.
        """
        print(self.get_text("select_language"))
        choice = input().strip()
        
        if choice == "1":
            self.current_language = "en"
        elif choice == "2":
            self.current_language = "uk"
        else:
            print(self.get_text("error").format("Invalid choice"))
            return False
        
        # Save language preference
        self.storage.save(self.current_language)
        
        print(self.get_text("language_changed"))
        return True