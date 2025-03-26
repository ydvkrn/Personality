const axios = require('axios');
const fs = require('fs');

// ✅ API से डेटा लाने के लिए लिंक सेट करो
const jsonURL1 = 'http://msmpr.free.nf/profiles.json'; // 1m.json के लिए
const jsonURL2 = 'http://msmpr.free.nf/reels.json';    // 2m.json के लिए

// ✅ लोकल JSON फाइलें
const file1 = 'reels:json';
const file2 = 'profiles.json';

// ✅ डेटा अपडेट करने का फंक्शन
async function updateJSON(url, file) {
    try {
        const response = await axios.get(url);
        const newData = response.data;

        let existingData = [];
        if (fs.existsSync(file)) {
            existingData = JSON.parse(fs.readFileSync(file, 'utf8'));
        }

        // ✅ profiles.json में "miba kijhamal" नाम के डेटा को रखो
        if (file === file1) {
            existingData = newData.filter(item => item.name === "miba kijhamal");
        } 
        // ✅ reels.json में Random डेटा रखो
        else if (file === file2) {
            existingData = newData.sort(() => Math.random() - 0.5).slice(0, 10); // 10 Random Items
        }

        // ✅ JSON फाइल को अपडेट करो
        fs.writeFileSync(file, JSON.stringify(existingData, null, 2));

        console.log(`✅ ${file} updated successfully!`);
    } catch (error) {
        console.error(`❌ Error updating ${file}:`, error);
    }
}

// ✅ दोनों JSON फाइलों को अपडेट करो
(async () => {
    await updateJSON(jsonURL1, file1);
    await updateJSON(jsonURL2, file2);
})();
