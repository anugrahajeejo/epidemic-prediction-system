require('./db');
const fs = require('fs');
const csv = require('csv-parser');
const Disease = require('./models/Disease');

const files = ['dengue_processed.csv', 'malaria_processed.csv'];

async function importData() {
    for (let file of files) {
        const results = [];

        await new Promise((resolve, reject) => {
            fs.createReadStream(file)
                .pipe(csv())
                .on('data', (data) => {
                    results.push({
                        month: data.month,
                        temperature: Number(data.temperature),
                        rainfall: Number(data.rainfall),
                        humidity: Number(data.humidity),
                        cases: Number(data.cases),
                        outbreak: data.outbreak
                    });
                })
                .on('end', resolve)
                .on('error', reject);
        });

        try {
            await Disease.insertMany(results);
            console.log(file + " data inserted ✅");
        } catch (err) {
            console.log("Error inserting " + file, err);
        }
    }
}

importData();