# Security Policy

## Supported Versions

Currently, we only support the latest version of this project.

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take the security of this project seriously. If you discover a security vulnerability (such as a leaked API key or an injection flaw), please follow these guidelines:

### 1. Do Not Open a Public Issue
**Please do not** report security vulnerabilities through public GitHub issues, discussions, or pull requests. Publicly disclosing a vulnerability can put the application and its users at risk before a fix is available.

### 2. How to Report
Please report the vulnerability by contacting the repository owner directly via email:
**work.dev.doshi@gmail.com**

In your report, please include:
* A description of the vulnerability.
* Steps to reproduce the issue.
* Any relevant screenshots or logs.

### 3. Response Timeline
I will try to acknowledge your report within 48 hours and will keep you updated on the progress of a fix.

---

## 🔐 Best Practices for Contributors

### API Key Safety
This project relies on **Google Gemini API Keys**.
* **Never** commit your `.env` file or `secrets.toml` to GitHub.
* Ensure `.env` is listed in your `.gitignore` file.
* If you suspect an API key has been exposed, revoke it immediately in the Google Cloud Console and generate a new one.

### Input Validation
This project uses **LangChain** and **Pydantic** to sanitize inputs and outputs. If you are modifying the backend logic, please ensure all user inputs continue to be validated to prevent Prompt Injection attacks.
