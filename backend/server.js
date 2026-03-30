const express = require('express');
const app = express();

// Middleware
app.use(express.json()); // parse JSON
app.use((req, res, next) => { // simple CORS middleware
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

// Root route
app.get('/', (req, res) => {
    res.send("Backend is working!");
});

// Predict route
app.post('/predict', (req, res) => {
    const { temperature, humidity, rainfall } = req.body;
    console.log("PREDICT ROUTE HIT:", req.body);

    let prediction = "Low"; // default
    if (temperature > 28 && humidity > 75 && rainfall > 150) {
        prediction = "High";
    } else if (temperature > 23 && humidity > 60 && rainfall > 50) {
        prediction = "Medium";
    }

    res.json({ prediction });
});

// Start server
const PORT = 5001;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));