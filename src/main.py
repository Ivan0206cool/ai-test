"""
Daily Journal Application - Main Entry Point
"""

import click
from datetime import datetime
from journal import Journal


@click.group()
def cli():
    """Daily Journal Application - Track your thoughts and reflections"""
    pass


@cli.command()
@click.option('--title', prompt='Entry title', help='Title of your journal entry')
@click.option('--mood', prompt='How are you feeling? (1-10)', type=int, help='Rate your mood')
def new_entry(title, mood):
    """Create a new journal entry"""
    journal = Journal()
    try:
        entry = journal.create_entry(title, mood)
        click.echo(f"\n✓ New entry created: {entry['date']}")
        click.echo(f"Title: {title}")
        click.echo(f"Mood: {mood}/10\n")
    except Exception as e:
        click.echo(f"✗ Error creating entry: {str(e)}", err=True)


@cli.command()
@click.option('--date', help='View entry from specific date (YYYY-MM-DD)')
def view_entries(date):
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
            for entry in entries:
                click.echo(f"  📝 {entry['date']} - {entry['title']} (Mood: {entry['mood']}/10)")
        else:
            click.echo("  No entries found.")
    except Exception as e:
        click.echo(f"✗ Error viewing entries: {str(e)}", err=True)


@cli.command()
@click.option('--query', prompt='Search term', help='Search entries by keyword')
def search(query):
    """Search through journal entries"""
    journal = Journal()
    try:
        results = journal.search_entries(query)
        click.echo(f"\nSearch results for '{query}': ({len(results)} found)")
        
        if results:
            for entry in results:
                click.echo(f"  📝 {entry['date']} - {entry['title']}")
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
    except Exception as e:
        click.echo(f"✗ Error retrieving statistics: {str(e)}", err=True)


if __name__ == '__main__':
    cli()