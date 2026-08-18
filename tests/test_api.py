from fastapi.testclient import TestClient

from api.app import app


client = TestClient(app)


sample_customer = {
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 5,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "No",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "Yes",
    "StreamingMovies": "Yes",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 75.5,
    "TotalCharges": 377.5
}


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert "message" in response.json()


def test_prediction():
    response = client.post(
        "/predict",
        json=sample_customer
    )

    assert response.status_code == 200

    result = response.json()

    assert "churn_prediction" in result
    assert "churn_probability" in result

    assert result["churn_prediction"] in [0, 1]
    assert 0 <= result["churn_probability"] <= 1