// Statistics Page Functions

async function loadStatistics() {
    try {
        const response = await fetch(`${API_BASE}/stats`);
        const result = await response.json();
        
        if (result.success) {
            displayStatistics(result.data);
        }
    } catch (error) {
        console.error('Error loading statistics:', error);
    }
}

function displayStatistics(stats) {
    // Update main stats
    document.getElementById('stat-total').textContent = stats.total_entries;
    document.getElementById('stat-average').textContent = stats.average_mood.toFixed(1);
    document.getElementById('stat-tag').textContent = stats.most_common_tag || '-';
    
    // Display mood distribution
    displayMoodDistribution(stats.mood_distribution);
}

function displayMoodDistribution(distribution) {
    const container = document.getElementById('mood-bars');
    const maxCount = Math.max(...Object.values(distribution));
    
    let html = '';
    for (let mood = 1; mood <= 10; mood++) {
        const count = distribution[mood.toString()] || 0;
        const percentage = maxCount > 0 ? (count / maxCount) * 100 : 0;
        const emoji = getMoodEmoji(mood);
        
        html += `
            <div class="mood-bar">
                <div class="mood-bar-label">${emoji}</div>
                <div class="mood-bar-fill" style="height: ${Math.max(percentage, 10)}px;">${count > 0 ? count : ''}</div>
            </div>
        `;
    }
    
    container.innerHTML = html;
}

document.addEventListener('DOMContentLoaded', function() {
    loadStatistics();
});
