const mongoose = require('mongoose');

const diseaseSchema = new mongoose.Schema({
    month: String,
    temperature: Number,
    rainfall: Number,
    humidity: Number,
    cases: Number,
    outbreak: String
});

module.exports = mongoose.model("Disease", diseaseSchema);