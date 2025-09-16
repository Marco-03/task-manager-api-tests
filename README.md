
# Task Manager API - Automated Tests

![API Tests](https://github.com/Marco-03/task-manager-api-tests/actions/workflows/pytest.yml/badge.svg?branch=main)

## Overview

This repository contains an **automated test suite** for the [Task Manager API](https://github.com/Marco-03/task-manager-api) backend.  

The tests are written in **Python** using `pytest` and `requests` and cover:

- User signup and login (JWT authentication)
- Task creation, listing, updating, and deletion
- Edge cases and authorization failures

This project demonstrates **Python automation, API testing, and CI/CD integration** using GitHub Actions.

---

## Features

- Full **CRUD API tests** for Task Manager
- **Automated CI** via GitHub Actions:
  - Automatically pulls the latest backend repo
  - Starts the Flask backend in CI with a **testing SQLite database**
  - Runs all tests and reports results
- Portable: tests run without exposing sensitive production data

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip
- Optional: virtual environment (`venv`)

### Installation

1. Clone this repository:

```bash

git clone https://github.com/Marco-03/task-manager-api-tests.git
cd task-manager-api-tests

python -m pip install --upgrade pip
pip install -r requirements.txt

```
Make sure the backend is running (or let GitHub Actions handle it).

# Running Tests Locally

Set TESTING=1 to use a temporary SQLite database:
```bash

export TESTING=1
```
Run pytest:
```bash

pytest -v
```
All tests should pass if your backend is configured correctly.

Tests include user signup/login and task operations.
