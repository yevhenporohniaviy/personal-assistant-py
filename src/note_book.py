from collections import UserDict
from src.record import NoteRecord
from src.utils.storage import Storage
from io import StringIO

class NoteBook(UserDict):
    """Class for storing and managing notes"""
    def __init__(self):
        super().__init__()
        self.storage = Storage("note_book.pickle")
        # Load data from storage if available
        data = self.storage.load()
        if data:
            self.data = data
            # Migrate old records if needed
            self._migrate_records()
    
    def _migrate_records(self):
        """Migrate old Record objects to NoteRecord"""
        migrated = False
        for name, record in list(self.data.items()):
            # Check if record is not a NoteRecord
            if not hasattr(record, 'content') or not hasattr(record, 'tags'):
                # Create a new NoteRecord with default content
                new_record = NoteRecord(record.name.value, getattr(record, 'content', ""))
                # Copy any available attributes
                if hasattr(record, 'created_at'):
                    new_record.created_at = record.created_at
                if hasattr(record, 'updated_at'):
                    new_record.updated_at = record.updated_at
                
                # Replace old record with new one
                self.data[name] = new_record
                migrated = True
        
        # Save changes if any records were migrated
        if migrated:
            self.save()
    
    def add_record(self, record):
        """Add a new note record to the note book"""
        self.data[record.name.value] = record
        self.save()
        return True
    
    def find(self, name):
        """Find a note by name"""
        return self.data.get(name)
    
    def delete(self, name):
        """Delete a note by name"""
        if name in self.data:
            del self.data[name]
            self.save()
            return True
        return False
    
    def search(self, query):
        """Search notes by content"""
        query = query.lower()
        results = []
        
        for record in self.data.values():
            # Search in name
            if query in record.name.value.lower():
                results.append(record)
                continue
            
            # Search in content
            if query in record.content.lower():
                results.append(record)
        
        return results
    
    def search_by_tag(self, tag):
        """Search notes by tag"""
        # Remove # if present at the beginning
        if tag.startswith('#'):
            tag = tag[1:]
            
        tag = tag.lower()
        results = []
        
        for record in self.data.values():
            for note_tag in record.tags:
                if tag == note_tag.value.lower():
                    results.append(record)
                    break
        
        return results
    
    def sort_by_tags(self):
        """Sort all notes by tags alphabetically and group them by tag"""
        if not self.data:
            return {}
            
        # Create a dictionary to store notes grouped by tags
        result = {}
        
        # Group notes by tags
        for record in self.data.values():
            if record.tags:
                for tag in record.tags:
                    tag_value = tag.value.lower()
                    if tag_value not in result:
                        result[tag_value] = []
                    if record not in result[tag_value]:
                        result[tag_value].append(record)
            else:
                # Group notes without tags under a special key
                if "no_tags" not in result:
                    result["no_tags"] = []
                result["no_tags"].append(record)
        
        # Sort the dictionary by tag keys
        return dict(sorted(result.items()))
    
    def save(self):
        """Save note book to storage"""
        return self.storage.save(self.data)
    
    def __str__(self):
        """String representation of the note book"""
        output = StringIO()
        
        if not self.data:
            return "Note book is empty"
        
        output.write("Note Book:\n")
        for record in self.data.values():
            output.write(f"{record}\n")
            output.write("-" * 30 + "\n")
        
        return output.getvalue().strip()