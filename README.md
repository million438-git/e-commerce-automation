# 🛒 E-commerce Login Automation

Automated UI testing for an e-commerce login page using **Python + Playwright + Pytest**.

## ✅ Test Coverage (4 test cases)

| Test Case | Description | Status |
|-----------|-------------|--------|
| TC-01 | Successful login with valid credentials | ✅ PASSED |
| TC-02 | Locked-out user is blocked | ✅ PASSED |
| TC-03 | Invalid password shows error | ✅ PASSED |
| TC-04 | Empty fields show validation error | ✅ PASSED |

## 🛠️ Tech Stack

- **Language:** Python 3.14
- **Framework:** Playwright, Pytest
- **Pattern:** Page Object Model (POM)
- **Reporting:** pytest-html
- **CI/CD:** GitHub Actions (runs on every push + nightly at 2 AM)

## 🚀 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/million438-git/e-commerce-automation.git
cd e-commerce-automation

# 2. Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
playwright install

# 4. Run tests
pytest --headed
