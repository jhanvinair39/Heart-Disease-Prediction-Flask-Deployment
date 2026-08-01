# Heart Disease Prediction & Flask Deployment

## Overview

This project develops a machine learning model to predict the likelihood of heart disease using clinical parameters. The model is trained on the Heart Disease dataset using a Random Forest Classifier and deployed as a Flask web application. Users can enter patient details through a web interface and receive an instant prediction.

---

## Features

- Heart disease prediction using Machine Learning
- Random Forest Classification model
- Flask-based REST API
- Interactive web interface
- Ready for cloud deployment using Render

---

## Dataset

**Dataset:** Heart Disease Dataset

Features used:

- Age
- Sex
- Chest Pain Type (cp)
- Resting Blood Pressure (trestbps)
- Cholesterol (chol)
- Fasting Blood Sugar (fbs)
- Rest ECG (restecg)
- Maximum Heart Rate (thalach)
- Exercise Induced Angina (exang)
- Oldpeak
- Slope
- Number of Major Vessels (ca)
- Thal

Target Variable:

- target
  - 0 = No Heart Disease
  - 1 = Heart Disease

---

## Machine Learning Algorithm

Random Forest Classifier

---

## Model Performance

Accuracy:

**98%**

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- Joblib
- HTML
- CSS
- Render

---

## Project Structure

```
HeartDiseaseDeployment/
│
├── app.py
├── train_model.py
├── model.pkl
├── heart.csv
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project folder

```bash
cd HeartDiseaseDeployment
```

Install the required packages

```bash
pip install -r requirements.txt
```

Run the Flask application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## API Endpoint

### POST /predict

Accepts patient details in JSON format and returns a prediction.

Example Response

```json
{
  "prediction": "Heart Disease Detected"
}
```

---

## Render Deployment

**Live Demo:** https://heart-disease-prediction-flask-deployment.onrender.com

---

## Conclusion

This project demonstrates the complete machine learning deployment pipeline, from data preprocessing and model training to API development and cloud deployment. The Random Forest model achieved an accuracy of approximately 98%, providing reliable predictions for heart disease risk. During deployment, challenges such as configuring project dependencies, loading the trained model correctly, and preparing the application for cloud hosting were addressed. Deploying the model with Flask and Render highlights the importance of MLOps by transforming a trained machine learning model into a real-world web service that is accessible, reusable, and easy to maintain.

---

## Author

**Jhanvi Nair**
