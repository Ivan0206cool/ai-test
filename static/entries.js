// Entries Page Functions

async function loadAllEntries() {
    try {
        const response = await fetch(`${API_BASE}/entries`);
        const result = await response.json();
        
        if (result.success) {
            displayEntries(result.data);
        }
    } catch (error) {
        console.error('Error loading entries:', error);
    }
}

function displayEntries(entries) {
    const listEl = document.getElementById('entries-list');
    
    if (entries.length === 0) {
        listEl.innerHTML = '<p style="text-align: center; color: #999; padding: 2rem;">No entries found.</p>';
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
            ${entry.content ? `<div class="entry-content-preview">${escapeHtml(entry.content.substring(0, 150))}${entry.content.length > 150 ? '...' : ''}</div>` : ''}
            ${entry.tags && entry.tags.length > 0 ? `<div class="entry-tags">${entry.tags.map(tag => `<span class="tag">${escapeHtml(tag)}</span>`).join('')}</div>` : ''}
        </div>
    `).join('');
}

async function searchEntries(event) {
    event.preventDefault();
    
    const query = document.getElementById('search-query').value;
    
    if (!query.trim()) {
        loadAllEntries();
        return;
    }
    
    try {
        const response = await fetch(`${API_BASE}/search?q=${encodeURIComponent(query)}`);
        const result = await response.json();
        
        if (result.success) {
            displayEntries(result.data);
        } else {
            alert('Error: ' + result.error);
        }
    } catch (error) {
        alert('Error searching: ' + error);
    }
}

document.addEventListener('DOMContentLoaded', function() {
    loadAllEntries();
    
    const searchBtn = document.getElementById('search-btn');
    if (searchBtn) {
        searchBtn.addEventListener('click', searchEntries);
    }
    
    const searchInput = document.getElementById('search-query');
    if (searchInput) {
        searchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                searchEntries(e);
            }
        });
    }
});
