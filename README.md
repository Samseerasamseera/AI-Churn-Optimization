\# Customer Churn Prediction \& AI Model Optimization



An end-to-end machine learning project for predicting customer churn, comparing classical ML models, explaining predictions with SHAP, deploying the selected model through FastAPI, and benchmarking inference performance.



\## Project Overview



The goal of this project is to build a production-oriented customer churn prediction system while evaluating both predictive performance and computational efficiency.



The project covers:



\- Data preprocessing and exploratory analysis

\- Feature engineering

\- Classification model development

\- Class imbalance analysis

\- Model comparison

\- XGBoost performance benchmarking

\- SHAP-based model explainability

\- ML pipeline serialization

\- FastAPI deployment

\- Automated API testing

\- Inference latency and throughput benchmarking



\## Architecture



             CUSTOMER DATA
                   |
                   v
           DATA CLEANING
                   |
                   v
                EDA
       "Understand the data"
                   |
                   v
          PREPROCESSING
      "Convert data for ML"
                   |
                   v
            TRAIN MODELS
                   |
        +----------+----------+
        |          |          |
        v          v          v
   Logistic       RF       XGBoost
  Regression
        |          |          |
        +----------+----------+
                   |
                   v
           MODEL COMPARISON
                   |
                   v
          SELECT / ANALYZE
                   |
                   v
          SHAP EXPLAINABILITY
          "Why this prediction?"
                   |
                   v
            SAVE PIPELINE
                   |
                   v
              FastAPI
                   |
                   v
            /predict API
                   |
                   v
          CHURN PROBABILITY
                   |
                   v
        PERFORMANCE BENCHMARK

