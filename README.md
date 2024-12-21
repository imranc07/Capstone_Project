# Capstone Project

This project implements a Page Object Model (POM) structure and Data Driven Testing Framework for automated testing of the [Swag Labs](https://www.saucedemo.com/).

Website Link: https://www.saucedemo.com/

## Test Objective:

The objective of this project is to implement an automated testing framework for the [Swag Labs](https://www.saucedemo.com/) web application using Python Selenium. The primary goals are to:

- **Validate Functionalities:** Ensure the core functionalities of the Swag Labs platform (such as navigation, login, randomly adding to the cart, and checkout processes) work as expected.
- **Improve Test Maintenance:** Utilize a structured approach to separate web page interaction logic from test scripts, making it easier to maintain and extend as the application evolves.
- **Enhance Test Reusability:** Promote reusability of code for interactions with page elements, reducing duplication across test scripts.
- **Support Data-Driven Testing:** Leverage test data (stored in `TestData/data.py` and `TestData/testdata.xlsx`) to run multiple test scenarios with different input sets to verify robustness and edge case handling.
- **Increase Test Coverage:** Automate critical paths such as user authentication, button functionality, and error handling to ensure high test coverage across essential user flows.
- **Ensure Browser Compatibility:** Run tests across multiple browsers (e.g., Chrome, Firefox, Edge, Safari) to validate cross-browser compatibility and identify potential issues.
- **Enable Continuous Testing:** Integrate with continuous integration (CI) tools to run tests automatically, ensuring that new changes do not introduce regressions or break existing functionality.

By achieving these objectives, this project aims to create a robust, maintainable, and scalable test automation framework for the Swag Labs platform.

## Test Suite:

### Test Case-1:
1. Test whether you can log in using the usernames `standard_user`, `problem_user`, `performance_glitch_user`, and `locked_out_user` with the password `secret_sauce`.
2. Verify login success using cookies only.

### Test Case-2:
1. Test whether you can log in using the username `guvi_user` and password `Secret@123`.

### Test Case-3:
1. Test whether the Logout button is functioning.
2. Test whether the Logout button is visible.

### Test Case-4:
1. Test whether the Cart button is visible.

### Test Case-5:
1. There are six products mentioned in the inventory. Choose any four products out of the six randomly using Python. Write Python code to get four products randomly. Do not manually fetch the products.
2. Fetch the product names and prices.

### Test Case-6:
1. Randomly choose four products out of the six mentioned in the inventory using Python. Do not manually fetch the products.
2. Add the four products to the cart.
3. Verify that the cart button reflects the four products added.

### Test Case-7:
1. Click the cart button to verify the products you have added.
2. Fetch the product details from the cart.

### Test Case-8:
1. Click the checkout button, add your details (First Name, Last Name, and Pin Code/Zip Code) into the given input boxes, and click the Continue button.
2. Download a screenshot of the Checkout Overview in PNG/JPEG/JPG format.
3. Verify that the products and their details on the page match the products you added.
4. Press the Finish button and confirm your action.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup and Installation](#setup-and-installation)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)
- [License](#license)

## Features

- **Page Object Model (POM):** Separation of test logic and UI interactions. Each web page has its corresponding class defining methods for interacting with the elements on that page.
- **Pytest Framework:** Used to manage test cases, execute tests, and generate detailed reports.
- **Reusable Components:** Common actions like login, navigating to sections, and performing shutdown operations are encapsulated in reusable methods, improving maintainability.
- **Cross-Platform Compatibility:** The framework can be run across different environments, supporting various operating systems and web browsers.
- **Automation and Reporting:** Automates repetitive tests with detailed reports on test results, making it easier to monitor and debug test executions.

## Tech Stack

- **Programming Language**: Python
- **Modules**: random
- **Test Framework**: pytest and DDT
- **Automation Tool**: Selenium WebDriver
- **Reporting**: pytest-html
- **Browser Compatibility**: Microsoft Edge, Google Chrome, Mozilla Firefox, Safari
- **CI/CD Integration**: GitHub Actions

## Setup and Installation

To set up and run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/imranc07/Capstone_Project.git
   cd Capstone_Project
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python3 -m venv env
   source env/bin/activate  # For Windows, use `env\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory to store sensitive information such as login credentials and URLs. Example:
     ```
     BASE_URL=https://example.com
     USER_EMAIL=test@example.com
     USER_PASSWORD=yourpassword
     ```

## Running Tests

To execute tests, use the following commands:

1. **Run All Tests**:
   ```bash
   pytest
   ```

2. **Generate HTML Report**:
   ```bash
   pytest --html=Reports/test_report.html
   ```

3. **Run Tests by Marker** (e.g., only "login" tests):
   ```bash
   pytest TestScripts/test_04_CartPage.py::test_add_to_cart
   ```

4. **Headless Browser Execution**:
   - Set up tests to run in headless mode directly in your test script.

---

## Project Structure:
```
Capstone_Project/
│
├── PageObjects/                 # Contains Page Object Models for Swag Labs Web Application
│   ├── LoginPage.py             # Handles methods and elements for Login Page
│   ├── InventoryPage.py         # Handles methods and elements for Inventory Page
│   ├── CartPage.py              # Handles methods and elements for Cart Page
│   └── CheckoutPage.py          # Handles methods and elements for Checkout Page
│
├── Reports/                     # Contains HTML reports
│   └── test_report.html         # HTML reports generated by pytest
│
├── TestData/                    # Stores test data for the test cases
│   ├── data.py                  # Contains reusable test data
│   └── testdata.xlsx            # Contains reusable test data and test log
│
├── TestLocators/                # Stores locators for web elements
│   └── locators.py              # Contains locators for all web elements used in the tests
│
├── TestScripts/                 # Contains all test cases
│   ├── test_01_Login.py         # Test script for data-driven login functionality
│   ├── test_02_LoginPage.py     # Test cases for Swag Labs Login Page
│   ├── test_03_InventoryPage.py # Test cases for Swag Labs Home Page
│   ├── test_04_CartPage.py      # Test cases for Swag Labs Cart Page
│   └── test_05_CheckoutPage.py  # Test cases for Swag Labs Checkout Page
│
├── Utilities/                   # Contains utility files
│   └── excel_functions.py       # Script with functions for handling and testing Excel operations
│
├── requirements.txt             # Lists project dependencies
│
└── README.md                    # Project documentation
```

---

## License
This project is open-source and available under the **MIT License**.

    ```
    Feel free to adjust the content based on your specific project setup!
    ``` 