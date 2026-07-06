// Entry Detail Page Functions

async function loadEntryDetail() {
    const urlParams = new URLSearchParams(window.location.search);
    const entryId = window.location.pathname.split('/').pop();
    
    try {
        const response = await fetch(`${API_BASE}/entry/${entryId}`);
        const result = await response.json();
        
        if (result.success) {
            displayEntryDetail(result.data);
        } else {
            document.getElementById('entry-content').innerHTML = `<p style="color: red;">Error: ${result.error}</p>`;
        }
    } catch (error) {
        document.getElementById('entry-content').innerHTML = `<p style="color: red;">Error loading entry: ${error}</p>`;
    }
}

function displayEntryDetail(entry) {
    const contentEl = document.getElementById('entry-content');
    
    let html = `
        <a href="/entries" class="back-link">← Back to Entries</a>
        <div class="entry-detail-content">
            <h1 class="entry-detail-title">${escapeHtml(entry.title)}</h1>
            <div class="entry-detail-meta">
                <div><strong>Date:</strong> ${formatDate(entry.date)}</div>
                <div><strong>Mood:</strong> ${getMoodEmoji(entry.mood)} ${entry.mood}/10</div>
    `;
    
    if (entry.tags && entry.tags.length > 0) {
        html += `<div><strong>Tags:</strong> ${entry.tags.map(tag => `<span class="tag">${escapeHtml(tag)}</span>`).join('')}</div>`;
    }
    
    html += `</div>`;
    
    if (entry.content) {
        html += `<div class="entry-detail-body">${escapeHtml(entry.content)}</div>`;
    }
    
    html += `</div>`;
    
    contentEl.innerHTML = html;
}

document.addEventListener('DOMContentLoaded', function() {
    loadEntryDetail();
});
