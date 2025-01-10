# Automation Project

This project is designed to automate web-based applications using **Selenium WebDriver** and **Pytest**. It follows the **Page Object Model (POM)** pattern and integrates with **Allure** for reporting. The framework is structured to be modular, making it easier to add tests, page actions, and utilities.

---------------------------------------------------------------------------------------------------------

## Project Structure


### Folder Breakdown:

1. **`tests/`**: Contains the test files. Each test file corresponds to a specific feature or functionality.
   - **`test_login.py`**: Example test file for testing the login functionality.

2. **`pages/`**: Contains the Page Object files where web elements and actions for each page are defined.
   - **`login_page.py`**: Contains actions like logging in and interacting with login page elements.

3. **`utils/`**: Contains helper functions for various utilities, such as browser handling and setup.
   - **`browser_utils.py`**: Functions for setting up, cleaning up, and managing browser instances.

4. **`conftest.py`**: Contains shared Pytest fixtures for test setup (e.g., browser initialization, login setup).

5. **`requirements.txt`**: List of all required Python dependencies for the project.

6. **`pytest.ini`**: Configuration file for customizing Pytest behavior, such as enabling HTML reports or defining test options.

7. **`README.md`**: This file, providing an overview of the project and instructions for setup and use.

---------------------------------------------------------------------------------------------------------

