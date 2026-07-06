"""
Unit tests for Entry class
"""

import pytest
from src.entry import Entry


class TestEntry:
    """Test cases for Entry class"""
    
    def test_entry_creation(self):
        """Test creating a new entry"""
        entry = Entry("Test Title", 8, "Test content")
        
        assert entry.title == "Test Title"
        assert entry.mood == 8
        assert entry.content == "Test content"
        assert len(entry.id) > 0
    
    def test_add_tag(self):
        """Test adding tags to entry"""
        entry = Entry("Test", 5)
        entry.add_tag("work")
        entry.add_tag("important")
        
        assert "work" in entry.tags
        assert "important" in entry.tags
        assert len(entry.tags) == 2
    
    def test_duplicate_tags(self):
        """Test that duplicate tags are not added"""
        entry = Entry("Test", 5)
        entry.add_tag("work")
        entry.add_tag("work")
        
        assert len(entry.tags) == 1
    
    def test_remove_tag(self):
        """Test removing tags from entry"""
        entry = Entry("Test", 5)
        entry.add_tag("work")
        entry.remove_tag("work")
        
        assert "work" not in entry.tags
    
    def test_update_content(self):
        """Test updating entry content"""
        entry = Entry("Test", 5, "Original content")
        entry.update_content("Updated content")
        
        assert entry.content == "Updated content"
    
    def test_to_dict(self):
        """Test converting entry to dictionary"""
        entry = Entry("Test", 7, "Content")
        entry.add_tag("personal")
        
        entry_dict = entry.to_dict()
        
        assert entry_dict['title'] == "Test"
        assert entry_dict['mood'] == 7
        assert entry_dict['content'] == "Content"
        assert "personal" in entry_dict['tags']