const axios = require('axios');
const fs = require('fs');

// JSON API URLs (अपनी API लिंक यहां डालो)
const jsonURL1 = 'http://msmpr.free.nf/reels.json'; // Replace with real API URL
const jsonURL2 = 'http://msmpr.free.nf/profiles.json'; // Replace with real API URL

// Local JSON Files
const file1 = 'reels.json';
const file2 = 'profiles.json';

async function updateJSON(url, file) {
    try {
        // API से डेटा लो
        const response = await axios.get(url);
        const newData = response.data;

        // लोकल JSON फाइल पढ़ो
        let existingData = [];
        if (fs.existsSync(file)) {
            existingData = JSON.parse(fs.readFileSync(file, 'utf8'));
        }

        // नए डेटा को जोड़ो (डुप्लिकेट हटाने के लिए फ़िल्टर कर सकते हो)
        const updatedData = [...existingData, ...newData];

        // अपडेटेड डेटा को वापस लिखो
        fs.writeFileSync(file, JSON.stringify(updatedData, null, 2));

        console.log(`✅ ${file} updated successfully!`);
    } catch (error) {
        console.error(`❌ Error updating ${file}:`, error);
    }
}

// दोनों JSON फाइलों को अपडेट करो
(async () => {
    await updateJSON(jsonURL1, file1);
    await updateJSON(jsonURL2, file2);
})();
