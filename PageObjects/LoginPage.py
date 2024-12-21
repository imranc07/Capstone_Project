"""LoginPage.py contains Selenium scripts for interacting with the Swag Labs Login Page.
This script provides functionalities such as performing the login process, verifying logout 
button visibility, and logging out of the application.
"""

# Importing necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Importing exception handling classes
from selenium.common.exceptions import TimeoutException

# Importing WebDriver wait utilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Importing locators, test data
from TestLocators.locators import SwagLabsLocators
from TestData.data import SwagLabsData

class SwagLabsLoginPage:
    """
    This class contains methods to automate login-related functionality on the Swag Labs application.
    """

    driver = None  # Shared WebDriver instance

    def __init__(self):
        """
        Initializes the WebDriver if not already initialized.
        """
        if SwagLabsLoginPage.driver is None:
            SwagLabsLoginPage.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(SwagLabsLoginPage.driver, 10) # Explicit wait instance

    def start(self):
        """
        Sets up WebDriver and navigates to the login page.
        """
        self.driver.maximize_window()
        self.driver.get(SwagLabsData.login_url)
        return True

    def login(self):
        """
        Logs into the application using provided credentials.
        """
        try:
            # Enter username and password, then click the login button
            self.wait.until(EC.presence_of_element_located((By.ID, SwagLabsLocators.username_locator))).send_keys(SwagLabsData.username)
            self.wait.until(EC.presence_of_element_located((By.ID, SwagLabsLocators.password_locator))).send_keys(SwagLabsData.password)
            self.wait.until(EC.element_to_be_clickable((By.ID, SwagLabsLocators.login_button_locator))).click()
            return True


        except TimeoutException as error:
            # Handle exceptions.
            print(f"ERROR: Timeout while logging in - {error}")
            return False

    def is_logout_button_visible(self):
        """
        Verifies if the logout button is visible on the page.
        """
        try:
            # Check visibility of the logout button via the menu
            menu_button = self.wait.until(EC.element_to_be_clickable((By.ID, SwagLabsLocators.menu_button_locator)))
            menu_button.click()
            logout_button = self.wait.until(EC.visibility_of_element_located((By.ID, SwagLabsLocators.logout_button_locator)))
            return logout_button.is_displayed()
       
        except TimeoutException as error:
            # Handle exceptions.
            print(f"ERROR: Timeout while checking logout button visibility - {error}")
            return False

    def logout(self):
        """
        Logs out of the application by clicking the logout button.
        """
        try:
            # Click the logout button to log out
            logout_button = self.wait.until(EC.element_to_be_clickable((By.ID, SwagLabsLocators.logout_button_locator)))
            logout_button.click()
            return True

        except TimeoutException as error:
            # Handle exceptions.
            print(f"ERROR: Timeout while logging out - {error}")
            return False

    def shutdown(self):
        """
        Closes the WebDriver and resets the shared WebDriver instance.
        """
        self.driver.quit()
        SwagLabsLoginPage.driver = None  # Reset shared WebDriver instance
        return True