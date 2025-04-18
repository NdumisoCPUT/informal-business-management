# CHANGELOG

## [v1.0.0] - 2025-04-17

## Task 1: Class Implementation
- Implemented 8 core domain classes in `/src`:
  - `UserAccount`, `Order`, `Payment`, `InventoryItem`
  - `CashFlowEntry`, `PromotionalMessage`, `SystemSettings`, `SalesReport`
- Encapsulated all attributes with private access (`__`)
- Added method stubs for all behavior as per UML diagram
- Created `main.py` to demonstrate class interactions

## Task 2: Creational Design Patterns
- Created `/creational_patterns/` directory
- Implemented all 6 creational design patterns:
  - Simple Factory (for `PromotionalMessage`)
  - Factory Method (for `PaymentProcessor`)
  - Abstract Factory (for `InventoryItem` categories)
  - Builder (for `SalesReport`)
  - Prototype (for cloning `Order` templates)
  - Singleton (for `SystemSettingsManager`)
- Added `main.py` usage examples demonstrating all patterns

## Task 3: Unit Testing
- Created `/tests/` directory
- Wrote unit tests for each creational pattern using `pytest`
- Configured import paths for `creational_patterns` using `sys.path.insert(...)`
- Achieved 100% pass rate and 86% test coverage

## Coverage Reporting
- Used `pytest-cov` to generate test coverage
- Generated `htmlcov/index.html` as HTML coverage report
- Linked report in `README.md`
- Uploaded a screenshot for proof of coverage

## Repo Cleanup & Improvements
- Added `.gitignore` to exclude:
  - `__pycache__/`, `*.pyc`, `.coverage`, `.pytest_cache/`, and `htmlcov/`
- Removed accidentally tracked cache files using `git rm --cached`
- Logged testing improvements and setup fixes in GitHub Issues

## GitHub Project Board Updates
- Moved all completed items to the "Done" column
- Created issues for testing-related improvements
- Linked commits to issues using `Fix #` references
