from flask import Flask, render_template, request, jsonify
import numpy as np

app = Flask(__name__)

AREAS = ["North Zone","Central Zone","South Zone","East Zone","West Zone"]
DISEASES = ["dengue","malaria"]


@app.route("/")
def home():
    return render_template("index.html",areas=AREAS,diseases=DISEASES)


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    month = int(data["month"])
    temperature = float(data["temperature"])
    rainfall = float(data["rainfall"])
    humidity = float(data["humidity"])
    cases = int(data["cases"])

    # Risk scoring logic
    risk_score = 0

    if temperature > 28:
        risk_score += 20

    if rainfall > 10:
        risk_score += 25

    if humidity > 70:
        risk_score += 20

    if cases > 100:
        risk_score += 35

    probability = min(risk_score,100)

    if probability > 70:
        risk = "High"
        alert = True
        message = "High outbreak risk. Immediate preventive action required."

    elif probability > 40:
        risk = "Moderate"
        alert = False
        message = "Moderate outbreak risk. Monitor the situation."

    else:
        risk = "Low"
        alert = False
        message = "Low outbreak risk."

    return jsonify({
        "outbreak_probability": probability,
        "risk_level": risk,
        "alert": alert,
        "message": message
    })


@app.route("/chart-data")
def chart_data():

    months = ["Jan","Feb","Mar","Apr","May","Jun",
              "Jul","Aug","Sep","Oct","Nov","Dec"]

    dengue_cases = [10,15,20,40,60,80,70,65,50,30,20,15]
    malaria_cases = [5,10,18,30,45,60,55,50,40,25,15,10]

    return jsonify({
        "months": months,
        "dengue": dengue_cases,
        "malaria": malaria_cases
    })


if __name__ == "__main__":
    app.run(debug=True)