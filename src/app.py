"""
Flask Web Application for Daily Journal
"""

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from datetime import datetime
from src.journal import Journal
import os


def create_app():
    """Create and configure the Flask app"""
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    CORS(app)
    
    journal = Journal()
    
    # ============= Web Routes =============
    
    @app.route('/')
    def index():
        """Home page"""
        return render_template('index.html')
    
    @app.route('/entries')
    def entries_page():
        """View all entries page"""
        return render_template('entries.html')
    
    @app.route('/entry/<entry_id>')
    def entry_detail(entry_id):
        """View single entry page"""
        return render_template('entry_detail.html', entry_id=entry_id)
    
    @app.route('/stats')
    def stats_page():
        """Statistics page"""
        return render_template('stats.html')
    
    # ============= API Routes =============
    
    @app.route('/api/entries', methods=['GET'])
    def api_get_entries():
        """Get all entries (API)"""
        try:
            entries = journal.get_all_entries()
            return jsonify({
                'success': True,
                'data': entries,
                'count': len(entries)
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    @app.route('/api/entry/<entry_id>', methods=['GET'])
    def api_get_entry(entry_id):
        """Get a specific entry (API)"""
        try:
            entry = journal.get_entry_by_id(entry_id)
            if entry:
                return jsonify({
                    'success': True,
                    'data': entry
                })
            else:
                return jsonify({
                    'success': False,
                    'error': 'Entry not found'
                }), 404
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    @app.route('/api/entries/date/<date_str>', methods=['GET'])
    def api_get_entries_by_date(date_str):
        """Get entries by date (API)"""
        try:
            entries = journal.get_entry_by_date(date_str)
            return jsonify({
                'success': True,
                'data': entries,
                'count': len(entries)
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    @app.route('/api/search', methods=['GET'])
    def api_search():
        """Search entries (API)"""
        try:
            query = request.args.get('q', '')
            tag = request.args.get('tag', None)
            
            if not query:
                return jsonify({
                    'success': False,
                    'error': 'Query parameter required'
                }), 400
            
            results = journal.search_entries(query, tag)
            return jsonify({
                'success': True,
                'data': results,
                'count': len(results)
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    @app.route('/api/entries/tag/<tag>', methods=['GET'])
    def api_get_entries_by_tag(tag):
        """Get entries by tag (API)"""
        try:
            entries = journal.get_entries_by_tag(tag)
            return jsonify({
                'success': True,
                'data': entries,
                'count': len(entries)
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    @app.route('/api/stats', methods=['GET'])
    def api_get_stats():
        """Get statistics (API)"""
        try:
            stats = journal.get_statistics()
            return jsonify({
                'success': True,
                'data': stats
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    @app.route('/api/entry', methods=['POST'])
    def api_create_entry():
        """Create a new entry (API)"""
        try:
            data = request.get_json()
            
            # Validate required fields
            if not data.get('title') or not data.get('mood'):
                return jsonify({
                    'success': False,
                    'error': 'Title and mood are required'
                }), 400
            
            # Validate mood range
            mood = int(data['mood'])
            if not (1 <= mood <= 10):
                return jsonify({
                    'success': False,
                    'error': 'Mood must be between 1 and 10'
                }), 400
            
            entry = journal.create_entry(
                title=data['title'],
                mood=mood,
                content=data.get('content', ''),
                tags=data.get('tags', [])
            )
            
            return jsonify({
                'success': True,
                'message': 'Entry created successfully',
                'data': entry
            }), 201
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    @app.route('/api/health', methods=['GET'])
    def api_health():
        """Health check endpoint"""
        return jsonify({
            'success': True,
            'message': 'Daily Journal API is running',
            'timestamp': datetime.now().isoformat()
        })
    
    return app
