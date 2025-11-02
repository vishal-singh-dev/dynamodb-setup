# 🚀 FastAPI + AWS DynamoDB API

A simple and modern Python API built with **FastAPI** and **AWS DynamoDB**.  
This project demonstrates how to use the **lifespan event handler** for app startup/shutdown and structured configuration via `.env`.

---

## 🧩 Features

- ✅ Built with [FastAPI](https://fastapi.tiangolo.com/)
- 🪣 Uses [AWS DynamoDB](https://aws.amazon.com/dynamodb/) as a NoSQL database
- ⚙️ Clean environment variable handling with `python-dotenv`
- 🔐 Secure credential management (no hardcoded keys)
- 🧠 Modern **lifespan** lifecycle pattern (replaces deprecated `on_event`)
- 📚 Auto-generated Swagger docs at `/docs`

---

---

## ⚙️ Requirements

- Python 3.9+
- AWS credentials (Access Key, Secret Key)
- DynamoDB table will be created automatically on first startup

---

## 🧰 Installation

### 1️⃣ Clone and enter project directory
```bash
git clone api into your-folder
cd  your-folder

python -m venv venv
source venv/bin/activate      (# On Windows: venv\Scripts\activate)
pip install -r requirements.txt
create .env file and add these keys
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=region
TABLE_NAME=Users






