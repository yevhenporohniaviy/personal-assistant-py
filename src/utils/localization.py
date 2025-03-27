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
                "select_language": "Select language:\n1. English\n2. Українська\nEnter number: ",
                "multiple_suggestions": "Did you mean one of these?",
                "select_suggestion": "Enter number (or press Enter to skip): ",
                "search_results": "Search results:",
                "no_results": "No results found.",
                "search_query": "Enter search query: ",
                "search_criteria": "Search by:\n1. Name\n2. Phone\n3. Email\n4. Address\nEnter number: ",
                "tag_search_criteria": "Search by:\n1. Tag name\n2. Note content\nEnter number: ",
                "sort_criteria": "Sort by:\n1. Name\n2. Date\n3. Tags\nEnter number: ",
                
                # Contact management
                "contact_added": "Contact added successfully.",
                "contact_deleted": "Contact deleted successfully.",
                "contact_updated": "Contact updated successfully.",
                "contact_not_found": "Contact not found.",
                "enter_name": "Enter name: ",
                "enter_phone": "Enter phone number: ",
                "enter_email": "Enter email: ",
                "enter_birthday": "Enter birthday (YYYY-MM-DD): ",
                "enter_address": "Enter address: ",
                "invalid_phone": "Invalid phone number format.",
                "invalid_email": "Invalid email format.",
                "invalid_date": "Invalid date format.",
                "upcoming_birthdays": "Upcoming birthdays in the next {days} days:",
                "no_birthdays": "No upcoming birthdays.",
                
                # Note management
                "note_added": "Note added successfully.",
                "note_deleted": "Note deleted successfully.",
                "note_updated": "Note updated successfully.",
                "note_not_found": "Note not found.",
                "enter_note_name": "Enter note name: ",
                "enter_note_content": "Enter note content: ",
                "enter_tag": "Enter tag: ",
                "tag_added": "Tag added successfully.",
                "no_notes_found": "No notes found.",
                "notes_by_tag": "Notes by tag:",
                "no_tags": "Notes without tags:"
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
                
                # Contact management messages
                "contact_added": "Контакт успішно додано.",
                "contact_deleted": "Контакт успішно видалено.",
                "contact_updated": "Контакт успішно оновлено.",
                "contact_not_found": "Контакт не знайдено.",
                "enter_name": "Введіть ім'я: ",
                "enter_phone": "Введіть номер телефону: ",
                "enter_email": "Введіть email: ",
                "enter_birthday": "Введіть дату народження (РРРР-ММ-ДД): ",
                "enter_address": "Введіть адресу: ",
                "invalid_phone": "Неправильний формат номера телефону.",
                "invalid_email": "Неправильний формат email.",
                "invalid_date": "Неправильний формат дати.",
                "upcoming_birthdays": "Найближчі дні народження протягом {days} днів:",
                "no_birthdays": "Немає найближчих днів народження.",
                
                # Note management messages
                "note_added": "Нотатку успішно додано.",
                "note_deleted": "Нотатку успішно видалено.",
                "note_updated": "Нотатку успішно оновлено.",
                "note_not_found": "Нотатку не знайдено.",
                "enter_note_name": "Введіть назву нотатки: ",
                "enter_note_content": "Введіть вміст нотатки: ",
                "enter_tag": "Введіть тег: ",
                "tag_added": "Тег успішно додано.",
                "no_notes_found": "Нотаток не знайдено.",
                "notes_by_tag": "Нотатки за тегом:",
                "no_tags": "Нотатки без тегів:",
                
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
                "select_language": "Виберіть мову:\n1. English\n2. Українська\nВведіть номер: ",
                "multiple_suggestions": "Можливо, ви мали на увазі одну з цих команд?",
                "select_suggestion": "Введіть номер (або натисніть Enter для пропуску): ",
                "search_results": "Результати пошуку:",
                "no_results": "Результатів не знайдено.",
                "search_query": "Введіть пошуковий запит: ",
                "search_criteria": "Пошук за:\n1. Ім'я\n2. Телефон\n3. Email\n4. Адреса\nВведіть номер: ",
                "tag_search_criteria": "Пошук за:\n1. Назва тегу\n2. Вміст нотатки\nВведіть номер: ",
                "sort_criteria": "Сортувати за:\n1. Ім'я\n2. Дата\n3. Теги\nВведіть номер: ",
                "search_criteria": "Пошук за:\n1. Ім'я\n2. Телефон\n3. Email\n4. Адреса\nВведіть номер: ",
                "tag_search_criteria": "Пошук за:\n1. Назва тегу\n2. Вміст нотатки\nВведіть номер: ",
                "sort_criteria": "Сортувати за:\n1. Ім'я\n2. Дата\n3. Теги\nВведіть номер: ",
                "search_criteria": "Шукати за:\n1. Ім'ям\n2. Телефоном\n3. Email\n4. Адресою\nВведіть номер: ",
                "tag_search_criteria": "Шукати за:\n1. Назвою тегу\n2. Вмістом нотатки\nВведіть номер: ",
                "sort_criteria": "Сортувати за:\n1. Ім'ям\n2. Датою\n3. Тегами\nВведіть номер: "
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
        Returns commands sorted by relevance, with common prefixes prioritized.
        """
        commands = {}
        # Get all command keys (excluding descriptions and internal keys)
        command_keys = [key for key in self.translations["en"].keys() 
                       if not key.startswith("desc_") and not key.startswith("_")]
        
        # Sort commands to prioritize common command prefixes (like 'add', 'search', etc)
        command_keys.sort(key=lambda x: (x.split()[0] if ' ' in x else x, len(x)))
        
        for cmd in command_keys:
            translated_cmd = self.get_text(cmd)
            desc_key = f"desc_{cmd}"
            if desc_key in self.translations[self.current_language]:
                commands[translated_cmd] = self.translations[self.current_language][desc_key]
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