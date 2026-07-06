"""
Unit tests for Journal class
"""

import pytest
import os
import shutil
from src.journal import Journal


class TestJournal:
    """Test cases for Journal class"""
    
    @pytest.fixture
    def temp_journal(self):
        """Create temporary journal for testing"""
        test_dir = 'test_data/entries'
        journal = Journal(test_dir)
        yield journal
        
        # Cleanup
        if os.path.exists('test_data'):
            shutil.rmtree('test_data')
    
    def test_journal_creation(self, temp_journal):
        """Test creating a new journal"""
        assert os.path.exists(temp_journal.data_dir)
    
    def test_create_entry(self, temp_journal):
        """Test creating a journal entry"""
        entry = temp_journal.create_entry("Test Entry", 8, "Test content")
        
        assert entry['title'] == "Test Entry"
        assert entry['mood'] == 8
        assert entry['content'] == "Test content"
    
    def test_get_all_entries(self, temp_journal):
        """Test retrieving all entries"""
        temp_journal.create_entry("Entry 1", 7)
        temp_journal.create_entry("Entry 2", 8)
        
        entries = temp_journal.get_all_entries()
        assert len(entries) == 2
    
    def test_search_entries(self, temp_journal):
        """Test searching entries"""
        temp_journal.create_entry("Productive Day", 9, "Got a lot done")
        temp_journal.create_entry("Relaxing Day", 7, "Took it easy")
        
        results = temp_journal.search_entries("Productive")
        assert len(results) == 1
        assert results[0]['title'] == "Productive Day"
    
    def test_get_statistics(self, temp_journal):
        """Test getting journal statistics"""
        temp_journal.create_entry("Entry 1", 6)
        temp_journal.create_entry("Entry 2", 8)
        temp_journal.create_entry("Entry 3", 10)
        
        stats = temp_journal.get_statistics()
        
        assert stats['total_entries'] == 3
        assert stats['average_mood'] == 8.0