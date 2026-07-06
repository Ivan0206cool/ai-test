"""
Entry class representing a single journal entry
"""

from datetime import datetime
import uuid


class Entry:
    """Represents a single journal entry"""
    
    def __init__(self, title, mood, content='', tags=None):
        self.id = str(uuid.uuid4())
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.title = title
        self.mood = mood
        self.content = content
        self.tags = tags or []
    
    def add_tag(self, tag):
        """Add a tag to the entry"""
        if tag not in self.tags:
            self.tags.append(tag)
    
    def remove_tag(self, tag):
        """Remove a tag from the entry"""
        if tag in self.tags:
            self.tags.remove(tag)
    
    def update_content(self, content):
        """Update the entry content"""
        self.content = content
    
    def to_dict(self):
        """Convert entry to dictionary"""
        return {
            'id': self.id,
            'date': self.date,
            'title': self.title,
            'mood': self.mood,
            'content': self.content,
            'tags': self.tags
        }
    
    def __str__(self):
        return f"Entry({self.date}: {self.title})"