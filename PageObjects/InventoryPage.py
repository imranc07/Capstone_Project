"""InventoryPage.py contains Selenium scripts for automating interactions with the Swag Labs Home Page.

This script includes functionalities for:

1. Setting up and managing a WebDriver instance using Selenium.
2. Logging into the Swag Labs application by extending the SwagLabsLoginPage class.
3. Navigating the inventory page to fetch and manipulate product details.
4. Randomly selecting products from the inventory and displaying their details.
5. Handling exceptions and ensuring smooth script execution with WebDriverWait.
6. Closing the WebDriver instance to clean up resources after execution.

The primary goal of this script is to facilitate automated testing and interaction with the Swag Labs Home
Page, making it easier to verify application functionality and behavior.
"""

# Importing necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Importing exception handling classes
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

# Importing WebDriver wait utilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Importing random module for selecting random products
import random

# Importing locators, test data, and Swag Labs Login Page
from TestLocators.locators import SwagLabsLocators
from TestData.data import SwagLabsData
from PageObjects.LoginPage import SwagLabsLoginPage

class SwagLabsInventoryPage(SwagLabsLoginPage):
    """
    This class extends SwagLabsLoginPage to include functionality specific to the Swag Labs inventory page.
    """

    driver = None  # Shared WebDriver instance

    def __init__(self):
        """
        Initializes the WebDriver if not already initialized.
        """
        if SwagLabsInventoryPage.driver is None:
            SwagLabsInventoryPage.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver = SwagLabsInventoryPage.driver
        self.wait = WebDriverWait(self.driver, 15)  # Explicit wait instance

    def start(self):
        """
        Sets up the browser window, navigates to the login page, and maximizes the window.
        """
        self.driver.maximize_window()
        self.driver.get(SwagLabsData.login_url)
        return True

    def get_random_products(self):
        """
        Logs in to the application, waits for the inventory page to load, and selects 4 random products.
        """
        if not self.login():
            print("FAIL: User Login Failed")
            return False
        try:
            # Wait for the inventory items to load after login
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, SwagLabsLocators.inventory_item_locator)))

            # Fetch all product elements on the page
            product_elements = self.driver.find_elements(By.CLASS_NAME, SwagLabsLocators.inventory_item_locator)

            # Ensure there are enough products available to select 4 randomly
            if len(product_elements) < 4:
                print("FAIL: Not enough products available.")
                return False

            # Select 4 random products from the available products
            selected_products = random.sample(product_elements, 4)

            # Print details of the selected products
            print("\nDetails of 4 randomly selected products are:")
            for i, product in enumerate(selected_products):
                name = product.find_element(By.CLASS_NAME, SwagLabsLocators.inventory_item_name_locator).text
                price = product.find_element(By.CLASS_NAME, SwagLabsLocators.inventory_item_price_locator).text
                print(f"Product {i + 1}: {name}, Price: {price}")
            return selected_products

        except (TimeoutException, NoSuchElementException) as error:
            # Handle exceptions
            print(f"ERROR: Timeout or element not found - {error}")
            return False

    def shutdown(self):
        """
        Closes the WebDriver and resets the shared driver instance.
        """
        self.driver.quit()
        SwagLabsInventoryPage.driver = None  # Reset shared WebDriver instance
        return True