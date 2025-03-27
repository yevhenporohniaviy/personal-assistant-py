import pickle
import os

class Storage:
    """Class for saving and loading data from disk"""
    def __init__(self, filename):
        self.filename = filename
        self.data_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data")
        
        # Create data folder if it doesn't exist
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)
        
        self.filepath = os.path.join(self.data_folder, filename)
    
    def save(self, data):
        """Save data to disk"""
        try:
            with open(self.filepath, "wb") as file:
                pickle.dump(data, file)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def load(self):
        """Load data from disk"""
        if not os.path.exists(self.filepath):
            return None
        
        try:
            with open(self.filepath, "rb") as file:
                return pickle.load(file)
        except Exception as e:
            print(f"Error loading data: {e}")
            return None