"""
test_01_Login.py This script demonstrates data-driven testing using Selenium and Excel files.
It automates the login functionality of the Swag Labs webpage, performing multiple login attempts 
based on test data stored in an Excel file. The results of each test are logged back into the Excel file.
"""

# Importing necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

# Importing exception handling classes
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


# Importing WebDriver wait utilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Importing locators, test data, and utility functions
from TestLocators.locators import SwagLabsLocators
from TestData.data import SwagLabsData
from Utilities.excel_functions import ExcelFunctions

# Test class for Swag Labs data-driven testing
class TestSwagLabsLogin:

    def test_DDTF_login(self):
        """
        Performs data-driven login attempts using test data from an Excel file.
        """

        # Setting up the WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 10)

        # Maximize the browser window
        self.driver.maximize_window()

        # Navigating to the Swag Labs login page
        self.driver.get(SwagLabsData().login_url)


        try:
            # Load Excel file and sheet details
            self.excel_file = SwagLabsData().excel_file
            self.sheet_number = SwagLabsData().sheet_number

            # Initialize the Excel utility for data reading and writing
            self.excel = ExcelFunctions(self.excel_file, self.sheet_number)

            # Get the total number of rows with data in the Excel sheet
            total_rows = self.excel.row_count()

            # Loop through each row in the Excel sheet
            for row in range(2, total_rows + 1):
                # Read username and password from the Excel sheet
                username = self.excel.read_data(row, 5)
                password = self.excel.read_data(row, 6)

                # Validate username and password
                if not username or not password:
                    print(f"ERROR: Missing data in row {row}. Username or password is empty.")
                    self.excel.write_data(row, 7, datetime.today())
                    self.excel.write_data(row, 8, datetime.now().time())
                    self.excel.write_data(row, 9, "Test Fail - Missing Data")
                    continue  # Skip to the next row

                # Enter username and password into the login form
                self.wait.until(EC.presence_of_element_located((By.ID, SwagLabsLocators.username_locator))).send_keys(username)
                self.wait.until(EC.presence_of_element_located((By.ID, SwagLabsLocators.password_locator))).send_keys(password)
                self.wait.until(EC.element_to_be_clickable((By.ID, SwagLabsLocators.login_button_locator))).click()

                # Check for login success based on cookies and URL
                cookies = self.driver.get_cookies()
                # print("Retrieved cookies:", cookies)  # Debugging: Print all cookies

                # Check if any of the expected session cookies are present
                valid_users = ['standard_user', 'problem_user', 'performance_glitch_user', 'locked_out_user']
                session_cookie = next((cookie for cookie in cookies if cookie.get('name') == 'session-username' and cookie.get('value') in valid_users),None)

                if session_cookie:
                    print(f"SUCCESS: Login Successful for user: {session_cookie['value']}")
                    # Log success details in the Excel sheet
                    self.excel.write_data(row, 7, datetime.today())
                    self.excel.write_data(row, 8, datetime.now().time())
                    self.excel.write_data(row, 9, "Test Pass")

                    # Log out of the application
                    try:
                        self.wait.until(EC.presence_of_element_located((By.ID, SwagLabsLocators.menu_button_locator))).click()
                        self.wait.until(EC.element_to_be_clickable((By.ID, SwagLabsLocators.logout_button_locator))).click()
                        print("SUCCESS: Logged out Successfully.")

                    except TimeoutException:
                        print("ERROR: Logout failed. Resetting the session.")
                        self.driver.delete_all_cookies()
                        self.driver.refresh()
                        # self.wait.until(EC.presence_of_element_located((By.ID, SwagLabsLocators.username_locator)))  # Ensure back to login page

                else:
                    print(f"FAIL: Session cookie not found. Login likely failed.")
                    # Log failure details in the Excel sheet
                    self.excel.write_data(row, 7, datetime.today())
                    self.excel.write_data(row, 8, datetime.now().time())
                    self.excel.write_data(row, 9, "Test Fail")
                    self.driver.refresh()  # Refresh the page for the next attempt
 
        except (NoSuchElementException, TimeoutException) as login_error:
            # Handling exceptions
            print(f"ERROR: {login_error}")
            # Log error details in the Excel sheet
            self.excel.write_data(row, 7, datetime.today())
            self.excel.write_data(row, 8, datetime.now().time())
            self.excel.write_data(row, 9, f"Error: {login_error}")

        finally:
            # Close the WebDriver
            self.driver.quit()