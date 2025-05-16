# 🧩 Contributing to Informal Business Management System

Welcome, and thank you for your interest in contributing to this open-source project! We appreciate all contributions — whether it's fixing bugs, adding features, improving documentation, or helping with project management.

This document will guide you through setting up the project, following coding standards, choosing tasks, and submitting pull requests.

---

## 🛠 Prerequisites

Before contributing, make sure you have:

- ✅ Python 3.12 or higher
- ✅ Git
- ✅ pip
- ✅ A GitHub account
- ✅ Optional but recommended:
  - Visual Studio Code or PyCharm
  - `make` or Unix shell (Mac/Linux)

---

## ⚙️ Project Setup

Follow these steps to clone and run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/informal-business-management.git
cd informal-business-management
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App (FastAPI)

```bash
uvicorn src.api.main:app --reload
```

### 5. Run Tests

```bash
pytest
```

---

## 🧹 Coding Standards

To maintain consistency across the codebase:

### Formatting
- Use [`black`](https://black.readthedocs.io/en/stable/) to auto-format code.
  ```bash
  black .
  ```

### Linting
- Use [`flake8`](https://flake8.pycqa.org/) to detect code style issues.
  ```bash
  flake8
  ```

### Type Checking (optional)
- Use `mypy` for static typing checks.
  ```bash
  mypy src/
  ```

### Testing
- Use `pytest` for unit and integration testing.
  - Tests must be located in the `tests/` folder.
  - All new features or bug fixes must include test coverage.

---

## 🌱 Branching Strategy

- `main` – Stable release-ready code  
- `dev` – Development integration branch  
- `feature/<name>` – For new features  
- `bugfix/<name>` – For fixing bugs  
- `docs/<name>` – Documentation-only changes

Example:
```bash
git checkout -b feature/add-jwt-auth
```

---

## 🧾 Commit Message Guidelines

Follow conventional commit format:
```
<type>: <short description>

[optional body]

[optional footer]
```

Example:
```
feat: add endpoint for creating inventory item
fix: handle validation error on order creation
docs: update README with setup steps
```

Common types:
- `feat` – New feature
- `fix` – Bug fix
- `docs` – Documentation only
- `refactor` – Code refactoring
- `test` – Adding or updating tests

---

## 🗂️ Choosing an Issue

1. Go to the [Issues](../../issues) tab.
2. Pick any issue labeled:
   - `good-first-issue` (for newcomers)
   - `feature-request` (for enhancements)
3. Comment to indicate you're working on it.

---

## 🔁 Submitting a Pull Request

1. **Fork the repository**  
2. **Clone your fork locally**  
3. **Create a new branch**
   ```bash
   git checkout -b feature/add-new-api
   ```
4. **Write your code and tests**
5. **Push to your fork**
   ```bash
   git push origin feature/add-new-api
   ```
6. **Submit a Pull Request**
   - Link to the issue
   - Describe what was changed
   - Add screenshots if applicable

---

## ✅ Pull Request Checklist

- [ ] I followed the setup instructions
- [ ] I formatted code with `black`
- [ ] I ran `flake8` and fixed all warnings
- [ ] I wrote/updated tests
- [ ] I linked related issues in the PR
- [ ] I ran the full test suite using `pytest`

---

## 💬 Community Guidelines

- Be respectful and inclusive
- Follow the [Code of Conduct](./CODE_OF_CONDUCT.md) (if provided)
- Ask questions in GitHub Discussions or Issues
- Don't hesitate to suggest improvements!

---

Thank you for helping grow this project 💚
