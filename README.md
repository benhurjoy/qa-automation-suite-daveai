# 🧪 QA Automation Suite - DaveAI

This repository contains automated **UI**, **API**, and optional **Load** test cases to validate the functionality and behavior of the [DaveAI](https://www.iamdave.ai/) website using Python-based tools and frameworks.

---

## 📁 Project Structure

qa-automation-suite-daveai/
│
├── ui_tests.py         # Selenium-based UI test cases
├── api_tests.py        # REST API test cases using unittest + requests
├── load_test.py        # Optional Locust load testing script
├── requirements.txt    # Project dependencies
└── README.md           # This file

---

## Test Overview

###  UI Tests (`ui_tests.py`)
Automates tests for:
- Page title verification
- Presence of "Book a Demo" button
- Navigation behavior on button click
- Visibility of input fields (Name, Email)

### API Tests (`api_tests.py`)
Validates `https://reqres.in/api`:
- GET a valid user
- GET an invalid user (expect 404)
- POST to create a user
- POST with empty body

### Load Testing (`load_test.py`)
Simulates up to 10 concurrent users making GET requests using **Locust**.

---

## ⚙️ How to Run Tests

### ✅ 1. Install Dependencies

```bash
pip install -r requirements.txt
