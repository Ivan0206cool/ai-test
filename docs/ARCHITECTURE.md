# Daily Journal - Architecture

## System Architecture

```
┌─────────────────────────────────────────┐
│         CLI Interface (main.py)         │
│      - Create Entry                     │
│      - View Entries                     │
│      - Search Entries                   │
│      - View Statistics                  │
└────────────────┬────────────────────────┘
                 │
┌────────────────▼────────────────────────┐
│          Journal Class (journal.py)     │
│      - Entry Management                 │
│      - File I/O Operations              │
│      - Search & Filter                  │
└────────────────┬────────────────────────┘
                 │
┌────────────────▼────────────────────────┐
│          Entry Class (entry.py)         │
│      - Entry Representation             │
│      - Tag Management                   │
│      - Data Serialization               │
└────────────────┬────────────────────────┘
                 │
┌────────────────▼────────────────────────┐
│       Utilities (utils.py)              │
│      - Date Formatting                  │
│      - Validation                       │
│      - Calculations                     │
└────────────────┬────────────────────────┘
                 │
┌────────────────▼────────────────────────┐
│    File System (data/entries/)          │
│      - JSON Entry Files                 │
└─────────────────────────────────────────┘
```

## Component Details

### 1. **CLI Interface (main.py)**
- Entry point for the application
- Handles user commands and input
- Provides user-friendly command-line interface
- Uses Click framework for CLI management

**Commands:**
- `new-entry`: Create new journal entry
- `view-entries`: Display journal entries
- `search`: Search entries by keyword
- `stats`: Show journal statistics

### 2. **Journal Class (journal.py)**
- Core business logic for managing entries
- Handles file operations and storage
- Implements search and filtering functionality
- Manages entry persistence

**Methods:**
- `create_entry()`: Create new entry
- `get_all_entries()`: Retrieve all entries
- `get_entry_by_date()`: Filter by date
- `search_entries()`: Full-text search
- `get_statistics()`: Calculate stats

### 3. **Entry Class (entry.py)**
- Represents a single journal entry
- Manages entry data structure
- Handles tag management
- Provides serialization methods

**Attributes:**
- `id`: Unique identifier (UUID)
- `date`: Entry timestamp
- `title`: Entry title
- `mood`: Mood rating (1-10)
- `content`: Entry content
- `tags`: Associated tags

### 4. **Utilities (utils.py)**
- Helper functions for common tasks
- Date formatting and validation
- Mood calculations and emoji mapping
- Directory management

**Functions:**
- `format_date()`: Format timestamps
- `validate_mood()`: Validate mood values
- `calculate_mood_trend()`: Analyze mood patterns
- `get_mood_emoji()`: Visual mood representation

### 5. **Data Storage**
- JSON file-based storage
- One file per entry
- Filename format: `YYYY-MM-DD_HH-MM-SS.json`
- Stored in `data/entries/` directory

## Data Flow

```
User Input
    ↓
CLI (main.py)
    ↓
Journal (journal.py)
    ↓
Entry (entry.py)
    ↓
File System (JSON)
    ↓
Data Persistence
```

## Entry JSON Structure

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "date": "2026-07-06 10:30:45",
  "title": "Great Day at Work",
  "mood": 8,
  "content": "Had a productive meeting and finished my project.",
  "tags": ["work", "productive"]
}
```

## Future Enhancements

- [ ] Database support (SQLite/PostgreSQL)
- [ ] Web UI interface
- [ ] Export functionality (PDF, CSV)
- [ ] Cloud synchronization
- [ ] Mobile app
- [ ] Advanced analytics
- [ ] Encryption for privacy
- [ ] Multi-user support

## Performance Considerations

- JSON storage suitable for thousands of entries
- In-memory operations for search
- File system I/O optimized
- Future: Consider database for large datasets

## Security

- Local file storage (no cloud)
- No external API dependencies
- User responsible for data backups
- Future: Add encryption support

## Testing

- Unit tests for Entry class
- Integration tests for Journal class
- Test data in isolated directory
- 70%+ code coverage target
