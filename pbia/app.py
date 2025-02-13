from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pickle
import numpy as np
import os

app = Flask(__name__)

# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bia.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Database Model
class Process(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    function = db.Column(db.String(100), nullable=False)
    bci = db.Column(db.Integer, nullable=False)
    risk_exposure = db.Column(db.String(50), nullable=False)
    probability_of_failure = db.Column(db.Float, nullable=False)
    downtime_cost = db.Column(db.Float, nullable=False)
    wrt = db.Column(db.Float, nullable=False)
    mtd = db.Column(db.Float, nullable=False)
    rpo = db.Column(db.Float, nullable=False)
    rto = db.Column(db.Float, nullable=False)
    financial_impact = db.Column(db.Float, nullable=False)
    recovery_cost = db.Column(db.Float, nullable=False)

# Create Database
with app.app_context():
    db.create_all()

# 1. **Add Process API**
@app.route("/add_process", methods=["POST"])
def add_process():
    try:
        data = request.json
        new_process = Process(
            function=data["function"],
            bci=data["bci"],
            risk_exposure=data["risk_exposure"],
            probability_of_failure=data["probability_of_failure"],
            downtime_cost=data["downtime_cost"],
            wrt=data["wrt"],
            mtd=data["mtd"],
            rpo=data["rpo"],
            rto=data["rto"],
            financial_impact=data["financial_impact"],
            recovery_cost=data["recovery_cost"],
        )
        db.session.add(new_process)
        db.session.commit()
        return jsonify({"message": "Process added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# 2. **Predict Impact API**
@app.route("/predict_impact", methods=["POST"])
def predict_impact():
    try:
        # Load the model
        if not os.path.exists("model.pkl"):
            return jsonify({"error": "Model file not found"}), 500

        with open("model.pkl", "rb") as file:
            model = pickle.load(file)

        # Get user data from request
        data = request.json
        user_input = np.array([data["features"]])  # Expecting a list of numerical features

        # Make prediction
        prediction = model.predict(user_input)
        impact_mapping = {1: "None", 2: "Moderate", 3: "Catastrophic"}
        predicted_impact = impact_mapping.get(prediction[0], "Unknown")

        return jsonify({"predicted_impact": predicted_impact})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 3. **Delete Process API**
@app.route("/delete_process/<int:process_id>", methods=["DELETE"])
def delete_process(process_id):
    try:
        process = Process.query.get(process_id)
        if not process:
            return jsonify({"error": "Process not found"}), 404

        db.session.delete(process)
        db.session.commit()
        return jsonify({"message": "Process deleted successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run Flask App
if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0',port=8001)
    
