"""
Utility functions for the Daily Journal application
"""

from datetime import datetime
import os


def format_date(date_str):
    """Format date string to readable format"""
    try:
        dt = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        return dt.strftime('%A, %B %d, %Y at %I:%M %p')
    except ValueError:
        return date_str


def validate_mood(mood):
    """Validate mood value (1-10)"""
    try:
        mood_int = int(mood)
        return 1 <= mood_int <= 10
    except ValueError:
        return False


def get_data_directory():
    """Get or create data directory"""
    data_dir = 'data/entries'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    return data_dir


def calculate_mood_trend(entries):
    """Calculate mood trend from entries"""
    if not entries:
        return None
    
    moods = [entry['mood'] for entry in entries]
    
    if len(moods) < 2:
        return 'stable'
    
    recent_avg = sum(moods[:5]) / min(5, len(moods))
    older_avg = sum(moods[5:]) / max(1, len(moods) - 5)
    
    if recent_avg > older_avg + 0.5:
        return 'improving'
    elif recent_avg < older_avg - 0.5:
        return 'declining'
    else:
        return 'stable'


def get_mood_emoji(mood):
    """Get emoji representation of mood"""
    if mood <= 3:
        return '😞'
    elif mood <= 5:
        return '😐'
    elif mood <= 7:
        return '🙂'
    else:
        return '😊'