# Personal Assistant

A command-line personal assistant application that helps you manage contacts and notes. Supports both English and Ukrainian languages.

## Features

### Contact Management

- Add new contacts with names, addresses, phone numbers, email, and birthdays
- Search contacts by various criteria (e.g., by name)
- Edit and delete contacts
- Display contacts with upcoming birthdays
- Validate phone numbers and email addresses

### Note Management

- Add text notes
- Search, edit, and delete notes
- Add tags to notes
- Search and sort notes by tags

### Intelligent Assistant

- The assistant can analyze user input and suggest the closest command for execution

### Data Storage

- All data (contacts, notes) are stored on the hard disk in the user's folder
- The assistant can be restarted without data loss

## Installation

### Prerequisites

- Python 3.6 or higher

### Installation Steps

1. Clone the repository:

```
git clone https://github.com/yourusername/personal-assistant-py.git
cd personal-assistant-py
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

Run the application:

```
python main.py
```

Follow the on-screen instructions to use the personal assistant.

### Available Commands

- **add contact** - Add a new contact
- **search contacts** - Search contacts by criteria
- **edit contact** - Edit an existing contact
- **delete contact** - Delete a contact
- **birthdays** - Show contacts with upcoming birthdays
- **add note** - Add a new note
- **search notes** - Search notes by content
- **edit note** - Edit an existing note
- **delete note** - Delete a note
- **add tag** - Add a tag to a note
- **search by tag** - Search notes by tag
- **help** - Show available commands
- **change language** - Change the interface language
- **exit** - Exit the program

## Project Structure

```
final-project-python/
├── src/                    # Main directory containing the code
│   ├── address_book.py     # Class for working with the address book
│   ├── assistant.py        # Main assistant class
│   ├── field.py            # Base classes for fields
│   ├── note_book.py        # Class for working with notes
│   ├── record.py           # Class for working with records
│   └── utils/              # Helper utilities
├── data/                   # Directory for storing data
├── main.py                 # Entry point of the program
└── requirements.txt        # Project dependencies
```

# Персональний Помічник

Консольний додаток персонального помічника, який допомагає керувати контактами та нотатками. Підтримує англійську та українську мови.

## Функціонал

### Управління Контактами

- Додавання нових контактів з іменами, адресами, номерами телефонів, електронною поштою та днями народження
- Пошук контактів за різними критеріями (наприклад, за іменем)
- Редагування та видалення контактів
- Відображення контактів з найближчими днями народження
- Валідація номерів телефонів та адрес електронної пошти

### Управління Нотатками

- Додавання текстових нотаток
- Пошук, редагування та видалення нотаток
- Додавання тегів до нотаток
- Пошук та сортування нотаток за тегами

### Інтелектуальний Помічник

- Помічник може аналізувати введення користувача та пропонувати найближчу команду для виконання

### Зберігання Даних

- Усі дані (контакти, нотатки) зберігаються на жорсткому диску в папці користувача
- Помічник може бути перезапущений без втрати даних

## Встановлення

### Передумови

- Python 3.6 або вище

### Кроки Встановлення

1. Клонуйте репозиторій:

```
git clone https://github.com/yourusername/personal-assistant-py.git
cd personal-assistant-py
```

2. Встановіть необхідні залежності:

```
pip install -r requirements.txt
```

## Використання

Запустіть додаток:

```
python main.py
```

Слідуйте інструкціям на екрані для використання персонального помічника.

### Доступні Команди

- **додати контакт** - Додати новий контакт
- **пошук контактів** - Пошук контактів за критеріями
- **редагувати контакт** - Редагувати існуючий контакт
- **видалити контакт** - Видалити контакт
- **дні народження** - Показати контакти з найближчими днями народження
- **додати нотатку** - Додати нову нотатку
- **пошук нотаток** - Пошук нотаток за змістом
- **редагувати нотатку** - Редагувати існуючу нотатку
- **видалити нотатку** - Видалити нотатку
- **додати тег** - Додати тег до нотатки
- **пошук за тегом** - Пошук нотаток за тегом
- **допомога** - Показати доступні команди
- **змінити мову** - Змінити мову інтерфейсу
- **вихід** - Вийти з програми

## Структура Проекту

```
final-project-python/
├── src/                    # Основна директорія з кодом
│   ├── address_book.py     # Клас для роботи з адресною книгою
│   ├── assistant.py        # Основний клас помічника
│   ├── field.py           # Базові класи для полів
│   ├── note_book.py       # Клас для роботи з нотатками
│   ├── record.py          # Клас для роботи з записами
│   └── utils/             # Допоміжні утиліти
├── data/                  # Директорія для зберігання даних
├── main.py               # Точка входу в програму
└── requirements.txt      # Залежності проекту
```
