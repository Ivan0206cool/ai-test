# Daily Journal - User Guide

Welcome to your Daily Journal! This guide will help you get started.

## Getting Started

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Ivan0206cool/ai-test.git
cd ai-test
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python src/main.py
```

## Features

### Create a New Entry

```bash
python src/main.py new-entry
```

You'll be prompted to:
- Enter a title for your entry
- Rate your mood (1-10)
- Add the entry content

### View Your Entries

```bash
python src/main.py view-entries
```

This displays all your journal entries in chronological order (newest first).

To view entries from a specific date:
```bash
python src/main.py view-entries --date 2026-07-06
```

### Search Entries

```bash
python src/main.py search --query "keyword"
```

Find entries by searching for keywords in titles or content.

### View Statistics

```bash
python src/main.py stats
```

Get insights into your journaling:
- Total number of entries
- Average mood rating
- Date of your last entry

## Understanding Mood Ratings

Rate your mood on a scale of 1-10:

- **1-3**: Not feeling great
- **4-6**: Neutral / Mixed feelings
- **7-9**: Good mood
- **10**: Excellent / Amazing day

## Tips for Better Journaling

1. **Be consistent** - Try to journal daily
2. **Be honest** - Write what you truly feel
3. **Be reflective** - Use journaling to process emotions
4. **Add tags** - Categorize entries for easy searching
5. **Be detailed** - More details help you remember

## Data Storage

Your journal entries are stored in the `data/entries/` directory as JSON files. Each entry is saved with a timestamp filename.

## Privacy

Your journal data is stored locally on your computer. Keep the `data/` directory private and secure.

## Troubleshooting

### Entries not showing up

- Make sure you're in the correct directory
- Check if `data/entries/` directory exists
- Verify the JSON files are readable

### Can't create entries

- Ensure you have write permissions in the directory
- Check if `data/entries/` folder exists (it auto-creates if not)

## Keyboard Shortcuts (when applicable)

- `Ctrl+C`: Exit the application
- `Ctrl+D`: Cancel input

## Support

For issues or questions, please open an issue on GitHub.

Happy journaling! 📝