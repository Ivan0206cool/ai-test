"""
Daily Journal Application - Main Entry Point
With enhanced content/body support
"""

import click
from datetime import datetime
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from journal import Journal


@click.group()
def cli():
    """Daily Journal Application - Track your thoughts and reflections"""
    pass


@cli.command()
@click.option('--title', prompt='Entry title', help='Title of your journal entry')
@click.option('--mood', prompt='How are you feeling? (1-10)', type=int, help='Rate your mood')
@click.option('--interactive', is_flag=True, help='Write content interactively')
def new_entry(title, mood, interactive):
    """Create a new journal entry"""
    journal = Journal()
    
    # Validate mood
    if not (1 <= mood <= 10):
        click.echo("✗ Mood must be between 1 and 10", err=True)
        return
    
    # Get content
    if interactive:
        click.echo("\n📝 Enter your journal content (press Enter twice when done):")
        lines = []
        empty_lines = 0
        while True:
            try:
                line = input()
                if line == '':
                    empty_lines += 1
                    if empty_lines >= 2:
                        break
                    lines.append(line)
                else:
                    empty_lines = 0
                    lines.append(line)
            except EOFError:
                break
        content = '\n'.join(lines).rstrip()
    else:
        content = click.prompt('Entry content (optional)', default='', show_default=False)
    
    # Add tags
    tags_input = click.prompt('Tags (comma-separated, optional)', default='', show_default=False)
    tags = [tag.strip() for tag in tags_input.split(',') if tag.strip()]
    
    try:
        entry = journal.create_entry(title, mood, content, tags)
        click.echo(f"\n✓ New entry created: {entry['date']}")
        click.echo(f"Title: {title}")
        click.echo(f"Mood: {mood}/10")
        if tags:
            click.echo(f"Tags: {', '.join(tags)}")
        if content:
            click.echo(f"Content: {content[:100]}..." if len(content) > 100 else f"Content: {content}")
        click.echo()
    except Exception as e:
        click.echo(f"✗ Error creating entry: {str(e)}", err=True)


@cli.command()
@click.option('--date', help='View entry from specific date (YYYY-MM-DD)')
@click.option('--full', is_flag=True, help='Show full content')
def view_entries(date, full):
    """View journal entries"""
    journal = Journal()
    try:
        if date:
            entries = journal.get_entry_by_date(date)
            click.echo(f"\nEntries for {date}:")
        else:
            entries = journal.get_all_entries()
            click.echo(f"\nAll journal entries ({len(entries)} total):")
        
        if entries:
            for i, entry in enumerate(entries, 1):
                emoji = journal.get_mood_emoji(entry['mood'])
                click.echo(f"\n{i}. {emoji} {entry['date']} - {entry['title']} (Mood: {entry['mood']}/10)")
                
                if entry.get('tags'):
                    click.echo(f"   Tags: {', '.join(entry['tags'])}")
                
                if full and entry.get('content'):
                    click.echo(f"   Content:\n   {entry['content'][:200]}..." if len(entry['content']) > 200 else f"   Content:\n   {entry['content']}")
        else:
            click.echo("  No entries found.")
    except Exception as e:
        click.echo(f"✗ Error viewing entries: {str(e)}", err=True)


@cli.command()
@click.option('--entry-id', prompt='Entry ID', help='ID of the entry to view')
def view_entry(entry_id):
    """View a specific journal entry in detail"""
    journal = Journal()
    try:
        entry = journal.get_entry_by_id(entry_id)
        if entry:
            emoji = journal.get_mood_emoji(entry['mood'])
            click.echo(f"\n{emoji} {entry['date']} - {entry['title']}")
            click.echo(f"Mood: {entry['mood']}/10")
            if entry.get('tags'):
                click.echo(f"Tags: {', '.join(entry['tags'])}")
            if entry.get('content'):
                click.echo(f"\nContent:\n{entry['content']}")
        else:
            click.echo(f"✗ Entry with ID '{entry_id}' not found", err=True)
    except Exception as e:
        click.echo(f"✗ Error viewing entry: {str(e)}", err=True)


@cli.command()
@click.option('--query', prompt='Search term', help='Search entries by keyword')
@click.option('--tag', help='Filter by tag')
def search(query, tag):
    """Search through journal entries"""
    journal = Journal()
    try:
        results = journal.search_entries(query, tag)
        click.echo(f"\nSearch results for '{query}'" + (f" with tag '{tag}'" if tag else "") + f": ({len(results)} found)")
        
        if results:
            for i, entry in enumerate(results, 1):
                emoji = journal.get_mood_emoji(entry['mood'])
                click.echo(f"{i}. {emoji} {entry['date']} - {entry['title']}")
        else:
            click.echo("  No matching entries found.")
    except Exception as e:
        click.echo(f"✗ Error searching entries: {str(e)}", err=True)


@cli.command()
def stats():
    """View journal statistics"""
    journal = Journal()
    try:
        stats_data = journal.get_statistics()
        click.echo(f"\n📊 Journal Statistics:")
        click.echo(f"  Total entries: {stats_data['total_entries']}")
        click.echo(f"  Average mood: {stats_data['average_mood']:.1f}/10")
        click.echo(f"  Last entry: {stats_data['last_entry_date']}")
        if 'most_common_tag' in stats_data and stats_data['most_common_tag']:
            click.echo(f"  Most used tag: {stats_data['most_common_tag']}")
    except Exception as e:
        click.echo(f"✗ Error retrieving statistics: {str(e)}", err=True)


@cli.command()
@click.option('--port', default=5000, help='Port to run the web server on')
@click.option('--debug', is_flag=True, help='Run in debug mode')
def web(port, debug):
    """Launch web interface"""
    try:
        from app import create_app
        app = create_app()
        click.echo(f"\n🚀 Starting Daily Journal Web Interface...")
        click.echo(f"📱 Open your browser and go to: http://localhost:{port}")
        click.echo(f"Press Ctrl+C to stop\n")
        app.run(debug=debug, port=port, host='127.0.0.1')
    except Exception as e:
        click.echo(f"✗ Error starting web interface: {str(e)}", err=True)


if __name__ == '__main__':
    cli()