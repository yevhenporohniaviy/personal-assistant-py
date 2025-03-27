import difflib
from src.utils.localization import Localization

class InputParser:
    """Class for parsing user input and guessing commands with multilingual support"""
    def __init__(self, commands):
        self.commands = commands
        self.localization = Localization()
        # Create a mapping of translated commands to original commands
        self.command_mapping = {}
        for cmd in commands:
            # Check if this command has translations in the localization data
            for lang_code in self.localization.languages.keys():
                if lang_code != "en" and cmd in self.localization.translations["en"]:
                    # Get the translated version of this command
                    if cmd in self.localization.translations[lang_code]:
                        translated_cmd = self.localization.translations[lang_code][cmd]
                        if translated_cmd and translated_cmd != cmd:
                            self.command_mapping[translated_cmd] = cmd
    
    def parse_input(self, user_input):
        """Parse user input into command and arguments with multilingual support"""
        parts = user_input.strip().split(maxsplit=1)
        command = parts[0].lower() if parts else ""
        
        # Check if it's a multi-word command in any language
        if command in self.commands:
            args = parts[1:]
        else:
            # Try to find multi-word commands in English
            for cmd in self.commands:
                if len(cmd.split()) > 1 and user_input.lower().startswith(cmd.lower()):
                    command = cmd
                    # Extract arguments after the command
                    args_str = user_input[len(cmd):].strip()
                    args = [args_str] if args_str else []
                    return command, args
            
            # Try to find translated commands
            user_input_lower = user_input.lower()
            for translated_cmd, original_cmd in self.command_mapping.items():
                if user_input_lower.startswith(translated_cmd.lower()):
                    command = original_cmd
                    # Extract arguments after the command
                    args_str = user_input[len(translated_cmd):].strip()
                    args = [args_str] if args_str else []
                    return command, args
            
            # If no multi-word command found, use the first word as command
            args = parts[1:]
            
            # Check if the first word is a translated command
            if command in self.command_mapping:
                command = self.command_mapping[command]
        
        return command, args
    
    def guess_command(self, user_input):
        """Try to guess the command based on similarity with multilingual support"""
        first_word = user_input.strip().split()[0].lower() if user_input.strip() else ""
        
        if not first_word:
            return None
        
        # Get list of all command words (including first words of multi-word commands)
        command_words = []
        for cmd in self.commands:
            cmd_parts = cmd.split()
            command_words.append(cmd_parts[0].lower())
            if len(cmd_parts) > 1:
                command_words.append(cmd.lower())
        
        # Add translated commands to the list
        for translated_cmd in self.command_mapping.keys():
            translated_parts = translated_cmd.split()
            command_words.append(translated_parts[0].lower())
            if len(translated_parts) > 1:
                command_words.append(translated_cmd.lower())
        
        # Find closest match
        matches = difflib.get_close_matches(first_word, command_words, n=1, cutoff=0.6)
        
        if matches:
            match = matches[0]
            # Find the full command that starts with the matched word
            for cmd in self.commands:
                if cmd.lower() == match or cmd.lower().startswith(match + " "):
                    return cmd
            
            # Check if the match is a translated command
            for translated_cmd, original_cmd in self.command_mapping.items():
                if translated_cmd.lower() == match or translated_cmd.lower().startswith(match + " "):
                    return original_cmd
        
        return None