# PyTest Example Repository

This repository contains various **PyTest** examples that I practiced while learning **unit testing** in Python. The examples demonstrate different testing techniques, including **assertions, parameterization, and mocking**.

## Features
- **Assertions**: Basic and advanced assertion techniques.
- **Parameterization**: Running multiple test cases with different inputs.
- **Mocking**: Simulating dependencies and external services.
- **Organized Structure**: Code is structured into `source/` and `tests/` directories.

## 📂 Project Structure
```
PyTest-example/
│-- source/
│   ├── __init__.py
│   ├── my_functions.py
│   ├── school.py
│   ├── service.py
│   ├── shapes.py
│
│-- tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_my_functions.py
│   ├── test_school.py
│   ├── test_service.py
│   ├── test_shapes.py
```

## 🛠 Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/ShivamGupta-16/PyTest-example.git
cd PyTest-example
```

### 2️⃣ Create and Activate a Virtual Environment (Recommended)
```sh
python -m venv venv
# Activate the virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

## ✅ Running Tests
To execute all test cases, use the following command:
```sh
pytest
```
Run a specific test file:
```sh
pytest tests/test_my_functions.py
```
Run tests with detailed output:
```sh
pytest -v
```

## 📝 License
This project is licensed under the **MIT License**. Feel free to use and modify the code.

---
