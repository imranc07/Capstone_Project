"""
CartPage.py contains Selenium scripts for interacting with the Swag Labs Cart Page.
This script provides functionalities such as verifying cart button is visible or not, adding 
products to the cart, verifying the cart badge,and validating the cart page contents.
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

# Importing random module for product selection
import random

# Importing locators, test data, and Swag Labs Login Page
from TestLocators.locators import SwagLabsLocators
from TestData.data import SwagLabsData
from PageObjects.LoginPage import SwagLabsLoginPage

class SwagLabsCartPage(SwagLabsLoginPage):
    """
    SwagLabsCartPage class provides methods to interact with the cart functionality
    of Swag Labs. This class extends SwagLabsLoginPage for login capabilities.
    """
    driver = None  # Shared WebDriver instance

    def __init__(self):
        """
        Initializes the WebDriver if not already initialized.
        """
        if SwagLabsCartPage.driver is None:
            SwagLabsCartPage.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver = SwagLabsCartPage.driver
        self.wait = WebDriverWait(self.driver, 15)  # Explicit wait instance

    def start(self):
        """
        Sets up the WebDriver by maximizing the window and navigating to the login URL.
        """
        self.driver.maximize_window()
        self.driver.get(SwagLabsData.login_url)
        return True

    def is_cart_button_visible(self):
        """
        Logs in and checks if the cart button is visible on the page.
        """
        # Perform login before verifying cart button visibility
        if not self.login():
            print("FAIL: User login failed.")
            return False

        try:
            # Wait for the cart button to become visible
            cart_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, SwagLabsLocators.cart_link_locator)))

            # Check if the cart button is displayed
            if cart_button.is_displayed():
                print("SUCCESS: Cart button is visible.")
                return True
            else:
                print("FAIL: Cart button is not visible.")
                return False

        # Handle exceptions
        except (TimeoutException, NoSuchElementException) as error:
            print(f"ERROR: Exception while checking cart button visibility - {error}")
            return False

    def add_to_cart(self):
        """
        Logs in and adds four randomly selected products to the cart.
        """
        # Perform login before adding products to the cart
        if not self.login():
            print("FAIL: User login failed.")
            return False

        try:
            # Wait for inventory items to load
            self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, SwagLabsLocators.inventory_item_locator)))

            # Fetch product details from the inventory
            product_elements = self.driver.find_elements(By.CLASS_NAME, SwagLabsLocators.inventory_item_locator)

            # Ensure there are six products in the inventory
            if len(product_elements) != 6:
                print("FAIL: Inventory does not have exactly six products.")
                return False

            # Randomly select 4 products
            selected_products = random.sample(product_elements, 4)

            # Print details of randomly selected products
            print("\nDetails of 4 randomly selected products are:")
            selected_product_details = []

            # Loop through each selected product and extract details
            for product in selected_products:
                name = product.find_element(By.CLASS_NAME, SwagLabsLocators.inventory_item_name_locator).text
                price = product.find_element(By.CLASS_NAME, SwagLabsLocators.inventory_item_price_locator).text
                selected_product_details.append((name, price))

            # Loop through selected products and add them to the cart
            for i, (name, price) in enumerate(selected_product_details):
                print(f"Product {i + 1}: Name: {name}, Price: {price}")
                add_to_cart_button = selected_products[i].find_element(By.CLASS_NAME, SwagLabsLocators.add_to_cart_button_locator)
                add_to_cart_button.click()

            # Return the details of the selected products
            return selected_product_details

        # Handling exceptions
        except (TimeoutException, NoSuchElementException) as error:
            print(f"ERROR: Exception while adding products to cart - {error}")
            return False

    def verify_cart_badge(self):
        """
        Verifies that the cart badge displays the correct number of items.
        """
        try:
            # Wait for the cart badge to appear
            cart_badge = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, SwagLabsLocators.cart_badge_locator)))
            cart_count = int(cart_badge.text)

            # Check if the cart badge count is 4 (expected number of items added to the cart)
            if cart_count == 4:
                print("SUCCESS: Cart badge shows 4 items.")
                return True
            else:
                print(f"FAIL: Cart badge shows {cart_count} items instead of 4.")
                return False
        
        # Handling exceptions
        except (TimeoutException, NoSuchElementException) as error:
            print(f"ERROR: Exception while verifying cart badge - {error}")
            return False

    def verify_cart_page(self):
        """
        Verifies the contents of the cart page by comparing product details.
        """
        try:
            # Click on the cart button to navigate to the cart page
            cart_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, SwagLabsLocators.cart_link_locator)))
            cart_button.click()

            # Wait for cart page to load
            self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, SwagLabsLocators.cart_list_locator)))

            # Fetch product details from the cart
            cart_products = self.driver.find_elements(By.CLASS_NAME, SwagLabsLocators.cart_item_locator)

            # Check if the cart contains any products
            if not cart_products:
                print("FAIL: No products found in the cart.")
                return False

            # Collect details of products present in the cart
            cart_product_details = []
            for product in cart_products:
                name = product.find_element(By.CLASS_NAME, SwagLabsLocators.inventory_item_name_locator).text
                price = product.find_element(By.CLASS_NAME, SwagLabsLocators.inventory_item_price_locator).text
                cart_product_details.append((name, price))

            # Print details of products in the cart
            print("\nProducts in the Cart Page:")
            for i, (name, price) in enumerate(cart_product_details):
                print(f"Product {i + 1}: Name: {name}, Price: {price}")

            return cart_product_details

        # Handling exceptions
        except (TimeoutException, NoSuchElementException) as error:
            print(f"ERROR: Exception while verifying cart page - {error}")
            return False

    def shutdown(self):
        """
        Closes the WebDriver and resets the shared instance.
        """
        self.driver.quit()
        SwagLabsCartPage.driver = None
        return True