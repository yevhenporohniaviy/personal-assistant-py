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
        """
        Parse user input and return command and arguments.
        Translates commands from non-English languages to English.
        Now properly handles longer commands before shorter ones.
        """
        # Sort commands by length (longer first) to ensure
        # "show all notes" is checked before "show all"
        sorted_commands = sorted(self.commands, key=len, reverse=True)
        
        command = user_input.lower()
        args = ""
        
        # First check if the input starts with any of the sorted commands
        for cmd in sorted_commands:
            # Check original language
            if command.startswith(cmd):
                command = cmd
                args = user_input[len(cmd):].strip()
                return command, args
            
            # Check translated version if it exists in the mapping
            translated_cmd = self.localization.get_text(cmd)
            if command.startswith(translated_cmd):
                command = cmd  # Return English command
                args = user_input[len(translated_cmd):].strip()
                return command, args
        
        # If no command found, return the input as is
        return command, args
    
    def guess_commands(self, user_input):
        """
        Suggest similar commands based on user input.
        Returns a list of possible commands.
        """
        user_cmd = user_input.lower()
        
        # Create a list of commands in the current language
        current_lang_cmds = [self.localization.get_text(cmd) for cmd in self.commands]
        
        # Find similar commands using difflib
        matches = difflib.get_close_matches(user_cmd, current_lang_cmds, n=3, cutoff=0.6)
        
        # Map back to original commands
        result = []
        for match in matches:
            # If it's a translated command, map back to English
            for cmd in self.commands:
                if self.localization.get_text(cmd) == match:
                    result.append(cmd)
                    break
            else:
                # Direct match in English
                result.append(match)
        
        return result