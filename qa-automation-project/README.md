# QA Automation Project - Selenium & Pytest

## Overview

This project is a web automation testing framework built using Python, Selenium WebDriver, and Pytest.

The framework automates login-related test scenarios on a sample web application and demonstrates the basics of UI test automation, test execution, assertions, and reusable test setup using Pytest fixtures.

## Technologies Used

* Python 3.14
* Selenium WebDriver
* Pytest
* Git & GitHub

## Test Scenarios Covered

### 1. Valid Login Test

* Navigate to the login page
* Enter valid credentials
* Verify successful login message

### 2. Invalid Login Test

* Enter invalid credentials
* Verify error message is displayed

### 3. Logout Test

* Login with valid credentials
* Logout from the application
* Verify successful logout message

### 4. Page Title Validation

* Open the application
* Verify the page title is displayed correctly

## Project Structure

qa-automation-project/

├── tests/

│   ├── conftest.py

│   ├── test_login.py

│   ├── test_invalid_login.py

│   ├── test_logout.py

│   └── test_page_title.py

├── pages/

├── utils/

├── requirements.txt

└── README.md

## Installation

Clone the repository:

git clone https://github.com/akshararanjith/qa-automation-project.git

Navigate to the project folder:

cd qa-automation-project

Create a virtual environment:

python -m venv .venv

Activate the virtual environment:

Windows:
.venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

## Execute Tests

Run all tests:

pytest -v

## Learning Outcomes

* Selenium WebDriver automation
* Pytest framework fundamentals
* Test assertions
* Browser automation
* Reusable fixtures using conftest.py
* Git and GitHub version control

## Author

Akshara Ranjith
