# 📘 QA Automation Suite - DaveAI

This repository contains automated UI, API, and optional Load test cases to validate the functionality and behavior of the [DaveAI website](https://www.iamdave.ai/) using Python-based tools and frameworks.

---

## 🧾 Project Structure

```
qa-automation-suite-daveai/
│
├── ui_tests.py         # Selenium-based UI test cases
├── api_tests.py        # REST API test cases using unittest + requests
├── load_test.py        # Optional Locust load testing script
├── requirements.txt    # Project dependencies
└── README.md           # This file
```

---

## 🧪 Test Overview

### ✅ UI Tests (`ui_tests.py`)
Automates tests for:
- Page title verification
- Presence of **"Book a Demo"** button
- Navigation behavior when button is clicked
- Visibility of form input fields (Name, Email)

**Tools Used:**
- Selenium WebDriver
- Unittest

---

### ✅ API Tests (`api_tests.py`)
Validates REST endpoints from [reqres.in](https://reqres.in/api):

- ✅ GET a valid user (Expect `200 OK`)
- ✅ GET an invalid user (Expect `404 Not Found`)
- ✅ POST request to create a user

**Tools Used:**
- Python `unittest`
- `requests` library

---

### ⚙️ Load Testing (`load_test.py`)
Simulates concurrent users hitting an endpoint using Locust.

Test Plan:
- Simulate 5–10 concurrent users
- Maximum of 100 requests/day (as per constraints)

**Tools Used:**
- Locust

---

## ⚙️ Setup & Installation

1. **Clone the repository:**

```bash
git clone https://github.com/benhurjoy/qa-automation-suite-daveai.git
cd qa-automation-suite-daveai
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Tests

- **UI Tests:**

```bash
python ui_tests.py
```

- **API Tests:**

```bash
python api_tests.py
```

- **Load Tests (Locust):**

```bash
locust -f load_test.py
```

Then open [http://localhost:8089](http://localhost:8089) in your browser to simulate load.

---

## 📦 Requirements

Contents of `requirements.txt`:

```
selenium==4.10.0
requests==2.31.0
locust==2.24.1
```

---

## 👤 Author

**Gundeti Benhur Joy**  

---
