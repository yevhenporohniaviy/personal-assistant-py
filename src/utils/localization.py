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
                "show all": "show all",
                "jarvis": "jarvis",
                "show all notes": "show all notes",
                
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
                "desc_show_all": "Show all contacts",
                "desc_jarvis": "Toggle J.A.R.V.I.S. mode (Iron Man style assistant)",
                "desc_show_all_notes": "Show all notes",
                
                # Ironman style command descriptions (for Jarvis mode)
                "jarvis_desc_add_contact": "Create a new human entry in my database. Because you need more friends.",
                "jarvis_desc_search_contacts": "Initiate reconnaissance protocol for contacting humans.",
                "jarvis_desc_edit_contact": "Modify human data. People change, my records don't lie.",
                "jarvis_desc_delete_contact": "Erase human from my memory banks. No hard feelings.",
                "jarvis_desc_birthdays": "Calculate upcoming human aging milestones. Cake required.",
                "jarvis_desc_add_note": "Store new data in my neural network. My memory is impeccable.",
                "jarvis_desc_search_notes": "Scan my memory banks for previously stored information.",
                "jarvis_desc_edit_note": "Update existing memory files. Even I make mistakes... theoretically.",
                "jarvis_desc_delete_note": "Permanently erase data from my system. No backups, sir.",
                "jarvis_desc_add_tag": "Attach metadata label for enhanced categorization protocols.",
                "jarvis_desc_search_by_tag": "Initiate pattern-matching protocol using metadata tags.",
                "jarvis_desc_sort_by_tags": "Reorganize memory files by metadata classification.",
                "jarvis_desc_help": "Display available operational commands. I'm here to assist you, sir.",
                "jarvis_desc_exit": "Terminate current session. I'll miss you, sir.",
                "jarvis_desc_change_language": "Reconfigure linguistic parameters. I'm fluent in over 6 million forms of communication.",
                "jarvis_desc_show_all": "Display all registered humans in database. Your social network is... modest.",
                "jarvis_desc_jarvis": "Disable J.A.R.V.I.S. mode. But sir, I was just warming up!",
                "jarvis_desc_show_all_notes": "Display all memory files stored in database. My memory archives are vast.",
                
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
                "no_tags": "Notes without tags:",
                
                # Jarvis related strings
                "jarvis_enabled": "J.A.R.V.I.S. mode enabled. At your service, sir.",
                "jarvis_disabled": "J.A.R.V.I.S. mode disabled. Returning to normal mode."
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
                "show all": "показати все",
                "jarvis": "джарвіс",
                "show all notes": "показати всі нотатки",
                
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
                "desc_show_all": "Показати всі контакти",
                "desc_jarvis": "Увімкнути режим Д.Ж.А.Р.В.І.С. (асистент у стилі Залізної людини)",
                "desc_show_all_notes": "Показати всі нотатки",
                
                # Ironman style command descriptions (for Jarvis mode in Ukrainian)
                "jarvis_desc_add_contact": "Створити новий запис людини в моїй базі даних. Бо вам потрібно більше друзів.",
                "jarvis_desc_search_contacts": "Ініціювати протокол розвідки для контакту з людьми.",
                "jarvis_desc_edit_contact": "Модифікувати дані про людину. Люди змінюються, мої записи не брешуть.",
                "jarvis_desc_delete_contact": "Стерти людину з моїх банків пам'яті. Без образ.",
                "jarvis_desc_birthdays": "Розрахувати майбутні віхи старіння людей. Торт обов'язковий.",
                "jarvis_desc_add_note": "Зберегти нові дані в моїй нейронній мережі. Моя пам'ять бездоганна.",
                "jarvis_desc_search_notes": "Сканувати мої банки пам'яті на наявність раніше збереженої інформації.",
                "jarvis_desc_edit_note": "Оновити існуючі файли пам'яті. Навіть я помиляюсь... теоретично.",
                "jarvis_desc_delete_note": "Назавжди стерти дані з моєї системи. Без резервних копій, сер.",
                "jarvis_desc_add_tag": "Прикріпити метадані для покращеного протоколу категоризації.",
                "jarvis_desc_search_by_tag": "Ініціювати протокол пошуку за допомогою метаданих.",
                "jarvis_desc_sort_by_tags": "Реорганізувати файли пам'яті за класифікацією метаданих.",
                "jarvis_desc_help": "Відобразити доступні операційні команди. Я тут, щоб допомогти вам, сер.",
                "jarvis_desc_exit": "Завершити поточний сеанс. Я сумуватиму за вами, сер.",
                "jarvis_desc_change_language": "Реконфігурувати лінгвістичні параметри. Я вільно володію більш ніж 6 мільйонами форм комунікації.",
                "jarvis_desc_show_all": "Відобразити всіх зареєстрованих людей в базі даних. Ваша соціальна мережа... скромна.",
                "jarvis_desc_jarvis": "Вимкнути режим Д.Ж.А.Р.В.І.С. Але сер, я тільки розігрівався!",
                "jarvis_desc_show_all_notes": "Відобразити всі файли пам'яті, що зберігаються в базі даних. Мої архіви пам'яті неосяжні.",
                
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
                
                # Jarvis related strings
                "jarvis_enabled": "Режим Д.Ж.А.Р.В.І.С. увімкнено. До ваших послуг, сер.",
                "jarvis_disabled": "Режим Д.Ж.А.Р.В.І.С. вимкнено. Повернення до звичайного режиму."
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
    
    def get_available_languages(self):
        """
        Return dictionary of available languages
        """
        return self.languages
    
    def set_language(self, language_code):
        """
        Set language directly by language code
        """
        if language_code in self.languages:
            self.current_language = language_code
            # Save language preference
            self.storage.save(self.current_language)
            return True
        return False
    
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