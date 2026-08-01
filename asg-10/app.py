from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

# Create Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load("model.pkl")

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Prediction API
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Convert JSON input to DataFrame
        input_data = pd.DataFrame([data])

        # Predict
        prediction = model.predict(input_data)[0]

        # Return result
        if prediction == 1:
            result = "Heart Disease Detected"
        else:
            result = "No Heart Disease"

        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)