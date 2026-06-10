# Secure Coding Review

## Project Overview

This project was developed as part of the CodeAlpha Cyber Security Internship. The objective of this project is to analyze a vulnerable login application, identify security weaknesses, assess their risks, and recommend secure coding practices.

## Features

- Review of a vulnerable Python login system
- Identification of common security vulnerabilities
- Security risk assessment
- Secure coding recommendations
- Demonstration of SQL Injection vulnerability

## Vulnerabilities Identified

### 1. SQL Injection
User input is directly concatenated into SQL queries, allowing attackers to manipulate database operations.

### 2. Plain Text Password Storage
Passwords are stored and processed without encryption or hashing, increasing the risk of credential compromise.

### 3. Missing Input Validation
User inputs are not validated or sanitized before processing.

## Recommendations

- Use parameterized SQL queries
- Implement password hashing using bcrypt
- Validate and sanitize all user inputs
- Apply secure authentication practices
- Follow secure coding standards

## Technologies Used

- Python 3
- SQLite Database
- VS Code

## Project Structure

```text
CodeAlpha_SecureCodingReview
│
├── vulnerable_login.py
├── create_db.py
├── users.db
├── report.md
├── README.md
└── screenshots/
```

## Demo Credentials

Username: codealpha

Password: codealpha123

## Author

Nandani Dodiya

## Internship

CodeAlpha Cyber Security Internship

## Disclaimer

This project is created for educational and security awareness purposes only. The vulnerable code is intentionally designed to demonstrate common security flaws and should not be used in production environments.