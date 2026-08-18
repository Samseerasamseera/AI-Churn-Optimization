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



```text

Customer Data

&#x20;    |

&#x20;    v

Data Preprocessing

&#x20;    |

&#x20;    v

Feature Transformation

&#x20;    |

&#x20;    v

ML Models

&#x20;    |

&#x20;    +---- Logistic Regression

&#x20;    |

&#x20;    +---- Random Forest

&#x20;    |

&#x20;    +---- Balanced Random Forest

&#x20;    |

&#x20;    +---- XGBoost

&#x20;    |

&#x20;    v

Model Evaluation

&#x20;    |

&#x20;    v

SHAP Explainability

&#x20;    |

&#x20;    v

Saved ML Pipeline

&#x20;    |

&#x20;    v

FastAPI

&#x20;    |

&#x20;    v

Prediction API

