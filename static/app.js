// Main App Functions

const API_BASE = 'http://localhost:5000/api';

// Get mood emoji
function getMoodEmoji(mood) {
    if (mood <= 3) return '😞';
    if (mood <= 5) return '😐';
    if (mood <= 7) return '🙂';
    return '😊';
}

// Format date
function formatDate(dateStr) {
    const date = new Date(dateStr.split(' ')[0]);
    return date.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
}

// Load and display stats on home page
async function loadStats() {
    try {
        const response = await fetch(`${API_BASE}/stats`);
        const result = await response.json();
        
        if (result.success) {
            const stats = result.data;
            
            // Update stat cards
            const totalEl = document.getElementById('stat-total');
            const moodEl = document.getElementById('stat-mood');
            const lastEl = document.getElementById('stat-last');
            
            if (totalEl) totalEl.textContent = stats.total_entries;
            if (moodEl) moodEl.textContent = stats.average_mood.toFixed(1);
            if (lastEl) lastEl.textContent = stats.last_entry_date ? formatDate(stats.last_entry_date) : '-';
        }
    } catch (error) {
        console.error('Error loading stats:', error);
    }
}

// Load recent entries
async function loadRecentEntries() {
    try {
        const response = await fetch(`${API_BASE}/entries`);
        const result = await response.json();
        
        if (result.success) {
            const entries = result.data.slice(0, 5); // Get first 5
            const listEl = document.getElementById('recent-list');
            
            if (listEl) {
                if (entries.length === 0) {
                    listEl.innerHTML = '<p style="text-align: center; color: #999;">No entries yet. Create your first entry!</p>';
                    return;
                }
                
                listEl.innerHTML = entries.map(entry => `
                    <div class="entry-card" onclick="window.location.href='/entry/${entry.id}'">
                        <div class="entry-header">
                            <div>
                                <div class="entry-title">${escapeHtml(entry.title)}</div>
                                <div class="entry-date">${formatDate(entry.date)}</div>
                            </div>
                            <div class="entry-mood">${getMoodEmoji(entry.mood)}</div>
                        </div>
                        ${entry.content ? `<div class="entry-content-preview">${escapeHtml(entry.content.substring(0, 100))}${entry.content.length > 100 ? '...' : ''}</div>` : ''}
                        ${entry.tags && entry.tags.length > 0 ? `<div class="entry-tags">${entry.tags.map(tag => `<span class="tag">${escapeHtml(tag)}</span>`).join('')}</div>` : ''}
                    </div>
                `).join('');
            }
        }
    } catch (error) {
        console.error('Error loading recent entries:', error);
    }
}

// Create new entry
async function createEntry(event) {
    event.preventDefault();
    
    const formData = {
        title: document.getElementById('title').value,
        mood: parseInt(document.getElementById('mood').value),
        content: document.getElementById('content').value,
        tags: document.getElementById('tags').value.split(',').map(tag => tag.trim()).filter(tag => tag)
    };
    
    try {
        const response = await fetch(`${API_BASE}/entry`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });
        
        const result = await response.json();
        
        if (result.success) {
            alert('Entry created successfully!');
            document.getElementById('entry-form').reset();
            document.getElementById('mood').value = 5;
            updateMoodDisplay();
            loadRecentEntries();
            loadStats();
        } else {
            alert('Error: ' + result.error);
        }
    } catch (error) {
        alert('Error creating entry: ' + error);
    }
}

// Update mood display
function updateMoodDisplay() {
    const mood = parseInt(document.getElementById('mood').value);
    document.getElementById('mood-display').textContent = mood;
    document.getElementById('mood-emoji').textContent = getMoodEmoji(mood);
}

// Escape HTML
function escapeHtml(text) {
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };
    return text.replace(/[&<>"']/g, m => map[m]);
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    // Bind entry form
    const entryForm = document.getElementById('entry-form');
    if (entryForm) {
        entryForm.addEventListener('submit', createEntry);
    }
    
    // Bind mood slider
    const moodSlider = document.getElementById('mood');
    if (moodSlider) {
        moodSlider.addEventListener('input', updateMoodDisplay);
        updateMoodDisplay();
    }
    
    // Load stats and recent entries
    loadStats();
    loadRecentEntries();
});
