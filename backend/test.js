require('./db');
const Disease = require('./models/Disease');

async function addData() {
    await Disease.create({
        disease: "Dengue",
        cases: 150,
        location: "Kochi",
        date: "2026-03-18"
    });

    console.log("Data inserted");
}

addData();
