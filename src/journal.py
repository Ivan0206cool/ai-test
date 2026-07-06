"""
Journal class to manage journal entries
"""

from datetime import datetime
from entry import Entry
import json
import os


class Journal:
    """Main Journal class for managing entries"""
    
    def __init__(self, data_dir='data/entries'):
        self.data_dir = data_dir
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
    
    def create_entry(self, title, mood, content=''):
        """Create a new journal entry"""
        entry = Entry(title, mood, content)
        self._save_entry(entry)
        return entry.to_dict()
    
    def get_all_entries(self):
        """Retrieve all journal entries"""
        entries = []
        if os.path.exists(self.data_dir):
            for filename in sorted(os.listdir(self.data_dir), reverse=True):
                if filename.endswith('.json'):
                    entry_data = self._load_entry_file(filename)
                    if entry_data:
                        entries.append(entry_data)
        return entries
    
    def get_entry_by_date(self, date_str):
        """Get entries for a specific date"""
        entries = []
        for entry in self.get_all_entries():
            if entry['date'].startswith(date_str):
                entries.append(entry)
        return entries
    
    def search_entries(self, query):
        """Search entries by keyword"""
        results = []
        query_lower = query.lower()
        
        for entry in self.get_all_entries():
            if (query_lower in entry['title'].lower() or 
                query_lower in entry['content'].lower()):
                results.append(entry)
        
        return results
    
    def get_statistics(self):
        """Get journal statistics"""
        entries = self.get_all_entries()
        
        if not entries:
            return {
                'total_entries': 0,
                'average_mood': 0,
                'last_entry_date': None
            }
        
        total_mood = sum(entry['mood'] for entry in entries)
        average_mood = total_mood / len(entries)
        
        return {
            'total_entries': len(entries),
            'average_mood': average_mood,
            'last_entry_date': entries[0]['date'] if entries else None
        }
    
    def _save_entry(self, entry):
        """Save entry to file"""
        filename = f"{entry.date.replace(' ', '_').replace(':', '-')}.json"
        filepath = os.path.join(self.data_dir, filename)
        
        with open(filepath, 'w') as f:
            json.dump(entry.to_dict(), f, indent=2)
    
    def _load_entry_file(self, filename):
        """Load entry from file"""
        filepath = os.path.join(self.data_dir, filename)
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return None