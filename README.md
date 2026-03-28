#  Network Security Anomaly Detection System

![Python Builder](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI Server](https://img.shields.io/badge/FastAPI-Framework-green)
![MLOps](https://img.shields.io/badge/MLOps-MLFlow%20%7C%20DagsHub-orange)
![Container](https://img.shields.io/badge/Docker-Ready-blueviolet)
![DB](https://img.shields.io/badge/MongoDB-Atlas-brightgreen)

##  Project Overview
The **Network Security Anomaly Detection System** is an end-to-end Machine Learning pipeline designed specifically to combat network security threats by accurately detecting **phishing** and **malicious network patterns**. 

This robust application fetches streaming or batch network data from a MongoDB cluster, processes it through an automated ML pipeline (Ingestion ➡️ Validation ➡️ Transformation ➡️ Model Training), and exposes the best-fitted model via a high-performance **FastAPI** web interface. Furthermore, the project embodies modern **MLOps** principles by utilizing **MLflow** and **DagsHub** for experiment tracking, and **Docker** for seamless, secure containerization.

## 🚀 Key Features
- **End-to-End Pipeline**: Fully automated modular components for ingestion, validation, processing, and training.
- **RESTful API Endpoint**: Batch predictions and model retraining accessible via intuitive FastAPI endpoints.
- **MLOps Integrated**: Artifacts, metrics, and models are continuously logged and saved.
- **Security-First Architecture**: Features strict input validation, non-root Docker execution, and robust CORS mitigation.
- **Cloud Database Integration**: Smooth connection to MongoDB Atlas.

---

##  System Architecture & Pipeline

1. **`Data Ingestion`**: Connects via TLS to MongoDB to extract real-world raw network security data and splits it into training/testing artifacts.
2. **`Data Validation`**: Implements schema inference and drift detection to ensure incoming data conforms to statistical expectations before processing.
3. **`Data Transformation`**: Handles null-value imputation (e.g., KNNImputer) and scales numerical inputs into normalized features.
4. **`Model Training`**: Fits multiple ML estimators (Random Forests, Logistic Regression, AdaBoost, etc.), tracks hyperparameters, and saves the most accurate predictive unit as `model.pkl` and `preprocessor.pkl`.
5. **`Model Deployment`**: Generates real-time batched predictions over CSV file uploads through an interactive FastAPI Swagger Dashboard.

---

##  Technology Stack
- **Core Language**: Python 3.10
- **Machine Learning**: `scikit-learn`, `pandas`, `numpy`
- **Backend Framework**: `FastAPI`, `Uvicorn`
- **Database**: `MongoDB (pymongo)`
- **Experiment Tracking**: `MLflow`, `DagsHub`
- **DevOps & Deployment**: `Docker`, `GitHub Actions`

---

##  Directory Structure

```text
📦 NetworkSecurity
├── 📂 networksecurity/          # Core Pipeline Modules
│   ├── components/              # Ingestion, Validation, Transform, Training scripts
│   ├── entity/                  # Configuration & Artifact entities
│   ├── constants/               # Environment & Global Variables
│   ├── pipeline/                # Full Training Pipeline Orchestrator
│   ├── logging/ & exception/    # Custom Error Handling & Logs
│   └── utils/                   # Shared Helper Functions
├── 📂 final_model/              # Scaler (preprocessor.pkl) & Best Model (model.pkl)
├── 📂 templates/                # Jinja2 HTML Templates for Prediction Outputs
├── 📝 app.py                    # FastAPI Server Application
├── 📝 main.py                   # CLI Pipeline Execution Script
├── 📝 push_data.py              # MongoDB Data Seeder script
├── 🐳 Dockerfile                # Secure Docker Image definition
├── 📄 requirements.txt          # Frozen, secure project dependencies
└── 📄 setup.py                  # PyPI Package Setup config
```

---

##  Installation & Setup

### 1️⃣ Local Development Setup

**1. Clone the repository**
```bash
git clone https://github.com/your-username/NetworkSecurity.git
cd NetworkSecurity
```

**2. Configure Environment Variables**
Create a `.env` file in the root directory containing your MongoDB connection details:
```env
MONGODB_URL_KEY="mongodb+srv://<user>:<password>@cluster.mongodb.net/?retryWrites=true&w=majority"
MONGO_DB_URL="mongodb+srv://<user>:<password>@cluster.mongodb.net/?retryWrites=true&w=majority"
```
*(Ensure `.env` is added to your `.gitignore` to prevent secret leaks!)*

**3. Create Virtual Environment & Install Dependencies**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**4. Initial Data Seeding (Optional)**
Push the sample phishing data to your MongoDB cluster:
```bash
python push_data.py
```

**5. Start the Application Server**
Launch the FastAPI server:
```bash
python app.py
```

---

## 🌐 API Reference & Usage

Once the server is running, navigate to `http://localhost:8000/docs` to access the Swagger UI.

### **1. `GET /train`**
Triggers the entire Machine Learning pipeline dynamically. It extracts fresh data from MongoDB, trains new models, tracks them in MLflow, and replaces the `final_model` artifacts.
- **Response**: `200 OK` (Training is successful)

### **2. `POST /predict`**
Accepts a `.csv` file upload containing batched network metrics.
- **Parameters**: `file` (UploadFile, Strict `.csv` validation)
- **Execution**: Applies the loaded preprocessor, feeds data into the active model, and appends a `predicted_column`.
- **Response**: Generates a visually formatted HTML Table rendering the prediction results.

---

