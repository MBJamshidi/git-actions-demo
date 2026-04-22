# git-actions-demo

![CI/CD](https://github.com/MBJamshidi/git-actions-demo/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A Python project demonstrating a professional **GitHub Actions CI/CD pipeline** with linting, multi-version testing, coverage reporting, and simulated deployment.

---

## Features

- Clean, typed calculator module (`add`, `subtract`, `multiply`, `divide`)
- Full pytest test suite with coverage reporting
- Automated linting with [Ruff](https://docs.astral.sh/ruff/)
- CI pipeline: lint → test (Python 3.9, 3.11, 3.12) → deploy
- GitHub Issue & PR templates

---

## Project Structure

```
git-actions-demo/
├── src/
│   ├── __init__.py
│   └── calculator.py       # Core calculator logic
├── tests/
│   ├── __init__.py
│   └── test_calculator.py  # pytest test suite
├── .github/
│   ├── workflows/
│   │   └── ci.yml          # CI/CD pipeline
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── PULL_REQUEST_TEMPLATE.md
├── pyproject.toml
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.9+

### Installation

```bash
git clone https://github.com/MBJamshidi/git-actions-demo.git
cd git-actions-demo
pip install -r requirements.txt
```

### Run Tests

```bash
pytest
```

### Run Linter

```bash
ruff check .
```

---

## CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/ci.yml`) runs automatically on every push and pull request to `main`:

| Job | What it does |
|-----|-------------|
| **Lint** | Checks code style with Ruff |
| **Test** | Runs pytest against Python 3.9, 3.11, and 3.12 |
| **Deploy** | Simulates production deployment (main branch only) |

---

## Usage

```python
from src.calculator import add, subtract, multiply, divide

add(2, 3)        # 5
subtract(10, 3)  # 7
multiply(4, 5)   # 20
divide(10, 2)    # 5.0
divide(5, 0)     # raises ValueError
```

---

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes
4. Open a Pull Request — the PR template will guide you

See [CONTRIBUTING](CONTRIBUTING.md) for more details.

---

## License

[MIT](LICENSE)
