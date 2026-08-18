import time
import requests


url = "http://127.0.0.1:8000/predict"


payload = {
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


# Warm-up request
requests.post(url, json=payload)


iterations = 100

start = time.perf_counter()

for _ in range(iterations):
    response = requests.post(
        url,
        json=payload
    )

total_time = time.perf_counter() - start

average_latency = total_time / iterations

print(f"Requests: {iterations}")
print(f"Total time: {total_time:.4f} seconds")
print(
    f"Average latency: "
    f"{average_latency * 1000:.2f} ms"
)
print(
    f"Requests/second: "
    f"{iterations / total_time:.2f}"
)