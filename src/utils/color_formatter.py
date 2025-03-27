from enum import Enum

class Color(Enum):
    """Color codes for terminal output"""
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class ColorFormatter:
    """Class for formatting text with colors"""
    @staticmethod
    def format(text, color):
        """Format text with specified color"""
        return f"{color.value}{text}{Color.RESET.value}"
    
    @staticmethod
    def success(text):
        """Format text as success message"""
        return ColorFormatter.format(text, Color.GREEN)
    
    @staticmethod
    def error(text):
        """Format text as error message"""
        return ColorFormatter.format(text, Color.RED)
    
    @staticmethod
    def warning(text):
        """Format text as warning message"""
        return ColorFormatter.format(text, Color.YELLOW)
    
    @staticmethod
    def info(text):
        """Format text as info message"""
        return ColorFormatter.format(text, Color.CYAN)
    
    @staticmethod
    def highlight(text):
        """Format text as highlighted message"""
        return ColorFormatter.format(text, Color.MAGENTA)
    
    @staticmethod
    def bold(text):
        """Format text as bold"""
        return ColorFormatter.format(text, Color.BOLD)
    
    @staticmethod
    def underline(text):
        """Format text as underlined"""
        return ColorFormatter.format(text, Color.UNDERLINE)