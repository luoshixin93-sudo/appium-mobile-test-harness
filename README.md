# Appium Mobile Test Harness

A lightweight, production-ready **mobile automation testing framework** built with **Appium + Python**, following the **Page Object Model (POM)** design pattern.

## Overview

This framework provides a scalable and maintainable structure for automating **native Android/iOS mobile applications**. It includes built-in support for HTML test reports, screenshot capture on failure, data-driven testing via Excel, and Jenkins CI/CD integration.

## Features

- **Page Object Model (POM)**: Clean separation of page logic and test code
- **HTML Test Reports**: Rich, visual test result reports
- **Automatic Screenshot Capture**: Screenshots attached to failed (and passed) test cases
- **Data-Driven Testing**: Excel-based test data for flexible scenario coverage
- **Jenkins Integration**: Run tests directly from Jenkins CI pipeline
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Prerequisites

- **Appium Server 2.0+**
- **Java 20+** (for Android SDK)
- **Python 3.8+**
- **Android SDK** (with `ANDROID_HOME` set)
- **Node.js 18+** and npm
- **Appium Python Client**: `pip install Appium-Python-Client`

## Quick Start

```bash
# Clone the repository
git clone https://github.com/luoshixin93-sudo/appium-mobile-test-harness
cd appium-mobile-test-harness

# Install Python dependencies
pip install -r requirements.txt

# Connect your Android device / emulator, then run:
pytest -m regression --html=reports/htmlreport/index.html --self-contained-html -s
```

## Project Structure

```
.
+-- pages/           # Page Object classes (UI page logic)
+-- utils/           # Locators, test data, common functions
+-- tests/           # Test case implementations
+-- app/             # APK files under test
+-- reports/         # HTML & Allure test reports
+-- config/          # Logging configuration
```

## Running Tests

```bash
# Full regression suite with HTML report
pytest -m regression --html=reports/htmlreport/report.html --self-contained-html -s

# With Allure report
allure serve reports/allure_report/
```

## Tech Stack

| Component        | Technology                     |
|------------------|--------------------------------|
| Automation Tool  | Appium 2.0                     |
| Language         | Python 3                        |
| Test Framework   | Pytest                          |
| Reports          | pytest-html, Allure             |
| Data Source      | Excel (.xlsx) via pandas        |
| CI/CD            | Jenkins                         |

---

Made with :heart: for cloud phone automation -> [qtphone.com](https://www.qtphone.com/)
