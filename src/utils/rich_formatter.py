from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.style import Style
from rich.prompt import Prompt, Confirm
from rich.progress import track
from rich import box
from colorama import init, Fore, Back, Style as ColoramaStyle
import random

# Initialize colorama
init(autoreset=True)

class RichFormatter:
    """Class for advanced text formatting using rich and colorama"""
    console = Console()
    # Jarvis mode flag
    jarvis_mode = False
    
    # Jarvis quotes for random selection
    jarvis_quotes = [
        "At your service, sir.",
        "What would you like me to do?",
        "Ready to assist, sir.",
        "All systems operational.",
        "Working at optimal capacity.",
        "I am here to assist you.",
        "How may I be of service today?",
        "Analysis complete. Awaiting further instruction.",
        "Indeed, sir. The suit is fully charged.",
        "I've prepared the usual protocols.",
        "Would you like me to run diagnostics?",
        "Current power levels at 100%."
    ]
    
    @staticmethod
    def toggle_jarvis_mode():
        """Toggle Jarvis mode on/off"""
        RichFormatter.jarvis_mode = not RichFormatter.jarvis_mode
        return RichFormatter.jarvis_mode
    
    @staticmethod
    def get_random_jarvis_quote():
        """Get a random Jarvis quote"""
        return random.choice(RichFormatter.jarvis_quotes)
    
    @staticmethod
    def print_header(text):
        """Print a stylized header"""
        if RichFormatter.jarvis_mode:
            RichFormatter.console.print(Panel(text, style="bold gold1", border_style="bold red", expand=False))
        else:
            RichFormatter.console.print(Panel(text, style="bold cyan", expand=False))
    
    @staticmethod
    def print_success(text):
        """Print a success message"""
        if RichFormatter.jarvis_mode:
            RichFormatter.console.print(f"[bold gold1]{text}[/bold gold1]")
        else:
            RichFormatter.console.print(f"[bold green]{text}[/bold green]")
        
    @staticmethod
    def print_error(text):
        """Print an error message"""
        if RichFormatter.jarvis_mode:
            RichFormatter.console.print(f"[bold red]Error detected: {text}[/bold red]")
        else:
            RichFormatter.console.print(f"[bold red]{text}[/bold red]")
        
    @staticmethod
    def print_warning(text):
        """Print a warning message"""
        if RichFormatter.jarvis_mode:
            RichFormatter.console.print(f"[bold dark_orange]Caution: {text}[/bold dark_orange]")
        else:
            RichFormatter.console.print(f"[bold yellow]{text}[/bold yellow]")
        
    @staticmethod
    def print_info(text):
        """Print an info message"""
        if RichFormatter.jarvis_mode:
            RichFormatter.console.print(f"[bold gold1]{text}[/bold gold1]")
        else:
            RichFormatter.console.print(f"[bold blue]{text}[/bold blue]")
    
    @staticmethod
    def display_contact(contact):
        """Display contact information in a rich panel"""
        # Check if contact has required attributes
        if not hasattr(contact, 'name'):
            RichFormatter.print_error("Invalid contact object: 'name' attribute missing")
            return
        
        content = Text()
        
        # Choose styles based on mode
        name_style = "bold gold1" if RichFormatter.jarvis_mode else "bold cyan"
        label_style = "red" if RichFormatter.jarvis_mode else "blue"
        value_style = "gold1" if RichFormatter.jarvis_mode else "cyan"
        highlight_style = "bold red" if RichFormatter.jarvis_mode else "bold magenta"
        border_style = "red" if RichFormatter.jarvis_mode else "cyan"
        
        content.append(f"Name: {contact.name.value}\n", style=name_style)
        
        if hasattr(contact, 'phones') and contact.phones:
            content.append("Phones:\n", style=label_style)
            for phone in contact.phones:
                content.append(f"  {phone.value}\n", style=value_style)
        
        if hasattr(contact, 'emails') and contact.emails:
            content.append("Emails:\n", style=label_style)
            for email in contact.emails:
                content.append(f"  {email.value}\n", style=value_style)
        
        if hasattr(contact, 'address') and contact.address:
            content.append("Address:\n", style=label_style)
            content.append(f"  {contact.address.value}\n", style=value_style)
        
        if hasattr(contact, 'birthday') and contact.birthday:
            content.append("Birthday:\n", style=label_style)
            content.append(f"  {contact.birthday.value}\n", style=value_style)
            if hasattr(contact, 'days_to_birthday'):
                days = contact.days_to_birthday()
                if days is not None:
                    if days == 0:
                        content.append("  🎂 Today is the birthday! 🎉\n", style=highlight_style)
                    else:
                        content.append(f"  Days to birthday: {days}\n", style=value_style)
        
        title = f"Contact: {contact.name.value}"
        if RichFormatter.jarvis_mode:
            title = f"📋 {title} [Database Entry]"
            
        RichFormatter.console.print(Panel(
            content,
            title=title,
            border_style=border_style,
            box=box.ROUNDED
        ))
    
    @staticmethod
    def display_note(note):
        """Display note information in a rich panel"""
        # Check if note has required attributes
        if not hasattr(note, 'name'):
            RichFormatter.print_error("Invalid note object: 'name' attribute missing")
            return
        
        # Choose styles based on mode
        title_style = "bold gold1" if RichFormatter.jarvis_mode else "bold magenta"
        label_style = "red" if RichFormatter.jarvis_mode else "blue"
        content_style = "gold1" if RichFormatter.jarvis_mode else "white"
        tag_style = "red" if RichFormatter.jarvis_mode else "magenta"
        border_style = "red" if RichFormatter.jarvis_mode else "magenta"
            
        content = Text()
        
        if hasattr(note, 'content') and note.content:
            content.append(f"Content:\n{note.content}\n\n", style=content_style)
        
        if hasattr(note, 'tags') and note.tags:
            content.append("Tags: ", style=label_style)
            for i, tag in enumerate(note.tags):
                content.append(f"#{tag.value} ", style=tag_style)
            content.append("\n")
        
        if hasattr(note, 'created_at'):
            content.append(f"Created: {note.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n", style="dim")
        if hasattr(note, 'updated_at'):
            content.append(f"Updated: {note.updated_at.strftime('%Y-%m-%d %H:%M:%S')}", style="dim")
        
        title = f"Note: {note.name.value}"
        if RichFormatter.jarvis_mode:
            title = f"📝 {title} [Memory File]"
            
        RichFormatter.console.print(Panel(
            content,
            title=title,
            border_style=border_style,
            box=box.ROUNDED
        ))
    
    @staticmethod
    def display_contacts_table(contacts):
        """Display contacts in a rich table"""
        # Choose styles based on mode
        title_style = "bold red on gold1" if RichFormatter.jarvis_mode else ""
        header_style = "red" if RichFormatter.jarvis_mode else "cyan"
        border_style = "red" if RichFormatter.jarvis_mode else ""
        box_type = box.HEAVY if RichFormatter.jarvis_mode else box.ROUNDED
        
        table = Table(title="Contacts", box=box_type, border_style=border_style, title_style=title_style)
        table.add_column("Name", style=header_style)
        table.add_column("Phones", style="gold1" if RichFormatter.jarvis_mode else "green")
        table.add_column("Email", style="dark_orange" if RichFormatter.jarvis_mode else "blue")
        table.add_column("Birthday", style="red" if RichFormatter.jarvis_mode else "magenta")
        
        for contact in contacts:
            # Skip invalid contacts
            if not hasattr(contact, 'name'):
                continue
                
            name = contact.name.value if hasattr(contact, 'name') else "Unknown"
            
            phones = ""
            if hasattr(contact, 'phones') and contact.phones:
                phones = ", ".join([phone.value for phone in contact.phones])
            
            email = ""
            if hasattr(contact, 'emails') and contact.emails:
                email = contact.emails[0].value
            
            birthday = ""
            if hasattr(contact, 'birthday') and contact.birthday:
                birthday = contact.birthday.value
            
            table.add_row(name, phones, email, birthday)
        
        RichFormatter.console.print(table)
    
    @staticmethod
    def display_notes_table(notes):
        """Display notes in a rich table"""
        # Choose styles based on mode
        title_style = "bold red on gold1" if RichFormatter.jarvis_mode else ""
        header_style = "red" if RichFormatter.jarvis_mode else "magenta"
        content_style = "gold1" if RichFormatter.jarvis_mode else "white"
        tag_style = "red" if RichFormatter.jarvis_mode else "magenta"
        border_style = "red" if RichFormatter.jarvis_mode else ""
        box_type = box.HEAVY if RichFormatter.jarvis_mode else box.ROUNDED
        
        table = Table(title="Notes", box=box_type, border_style=border_style, title_style=title_style)
        table.add_column("Title", style=header_style)
        table.add_column("Content Preview", style=content_style)
        table.add_column("Tags", style=tag_style)
        
        for note in notes:
            # Skip invalid notes
            if not hasattr(note, 'name'):
                continue
                
            name = note.name.value if hasattr(note, 'name') else "Unknown"
            
            content_preview = ""
            if hasattr(note, 'content') and note.content:
                content_preview = (note.content[:30] + "...") if len(note.content) > 30 else note.content
            
            tags = ""
            if hasattr(note, 'tags') and note.tags:
                tags = " ".join([f"#{tag.value}" for tag in note.tags])
            
            table.add_row(name, content_preview, tags)
        
        RichFormatter.console.print(table)

    @staticmethod
    def ask_input(prompt_text, default=""):
        """Ask for user input with rich formatting"""
        if RichFormatter.jarvis_mode:
            # Add a Jarvis-style prefix and style the text directly
            prompt_text = f"[bold red]J.A.R.V.I.S. > {prompt_text}[/bold red]"
        
        return Prompt.ask(prompt_text, default=default)
    
    @staticmethod
    def ask_confirm(prompt_text, default=False):
        """Ask for confirmation with rich formatting"""
        if RichFormatter.jarvis_mode:
            # Add a Jarvis-style prefix with styling
            prompt_text = f"[bold red]J.A.R.V.I.S. > {prompt_text}[/bold red]"
            
        return Confirm.ask(prompt_text, default=default)
    
    @staticmethod
    def show_progress(iterable, description="Processing"):
        """Show a progress bar for an operation"""
        if RichFormatter.jarvis_mode:
            description = f"Running {description} protocol"
            
        return track(iterable, description=description)
        
    @staticmethod
    def print_jarvis_welcome():
        """Print Jarvis welcome message"""
        RichFormatter.console.print(Panel(
            "J.A.R.V.I.S. initialized. All systems online.",
            title="JARVIS - Just A Rather Very Intelligent System",
            style="bold gold1",
            border_style="bold red",
            box=box.HEAVY
        ))
        RichFormatter.print_info(RichFormatter.get_random_jarvis_quote())

# Colorama examples for direct use
def colorama_example():
    # Foreground colors
    print(Fore.RED + "Red text")
    print(Fore.GREEN + "Green text")
    print(Fore.BLUE + "Blue text")
    
    # Background colors
    print(Back.WHITE + Fore.BLACK + "Black text on white background")
    
    # Styles
    print(ColoramaStyle.BRIGHT + "Bright text")
    print(ColoramaStyle.DIM + "Dim text")
    
    # Reset all styling
    print(ColoramaStyle.RESET_ALL + "Normal text") 