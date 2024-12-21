"""
CheckoutPage.py contains Selenium scripts for interacting with the Swag Labs Checkout Page.
This script provides functionalities such as performing the checkout process, verifying the 
checkout overview, and capturing screenshots of the checkout page.
"""

# Importing necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Importing exception handling classes
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException

# Importing WebDriver wait utilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Importing locators and test data
from TestLocators.locators import SwagLabsLocators
from TestData.data import SwagLabsData
from PageObjects.CartPage import SwagLabsCartPage

class SwaglabsCheckoutPage(SwagLabsCartPage):
    """
    SwaglabsCheckoutPage class provides methods to interact with the checkout functionality
    of Swag Labs. This class extends SwagLabsCartPage for cart functionalities.
    """

    driver = None  # Shared WebDriver instance

    def __init__(self):
        """
        Initializes the WebDriver if not already initialized.
        """
        if SwaglabsCheckoutPage.driver is None:
            SwaglabsCheckoutPage.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver = SwaglabsCheckoutPage.driver
        self.wait = WebDriverWait(self.driver, 15)  # Explicit wait instance

    def start(self):
        """
        Sets up the WebDriver by maximizing the window and navigating to the login URL.
        """
        self.driver.maximize_window()
        self.driver.get(SwagLabsData.login_url)
        return True

    def checkout(self):
        """
        Performs the checkout process by adding items to the cart, filling out checkout details,
        and navigating to the checkout overview page.
        """
        if not self.add_to_cart():
            print("FAIL: No products found in the cart.")
            return False

        try:
            # Click on the cart button to navigate to the cart page
            cart_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, SwagLabsLocators.cart_link_locator)))
            cart_button.click()

            # Wait for the cart page to load
            self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, SwagLabsLocators.cart_list_locator)))

            # Click the checkout button to begin the checkout process
            checkout_button = self.wait.until(EC.element_to_be_clickable((By.ID, SwagLabsLocators.checkout_button_locator)))
            checkout_button.click()

            # Enter checkout information (First Name, Last Name, Postal Code)
            self.wait.until(EC.presence_of_element_located((By.ID, SwagLabsLocators.first_name_locator))).send_keys(SwagLabsData.first_name)
            self.wait.until(EC.presence_of_element_located((By.ID, SwagLabsLocators.last_name_locator))).send_keys(SwagLabsData.last_name)
            self.wait.until(EC.presence_of_element_located((By.ID, SwagLabsLocators.postal_code_locator))).send_keys(SwagLabsData.postal_code)

            # Click the continue button to proceed to the overview page
            continue_button = self.wait.until(EC.element_to_be_clickable((By.ID, SwagLabsLocators.continue_button)))
            continue_button.click()

            return True 

        # Handling exceptions    
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print(f"ERROR during checkout: {error}")
            return False

    def capture_screenshot(self):
        """
        Captures a screenshot of the Checkout Overview page and saves it locally.
        """
        try:
            # Locate the checkout overview section and capture a screenshot
            checkout_overview = self.wait.until(EC.presence_of_element_located((By.ID, SwagLabsLocators.checkout_summary_locator)))
            checkout_overview.screenshot('checkout_overview.png')
            print("SUCCESS: Screenshot of the checkout overview page captured.")
            return True

        # Handling exceptions
        except TimeoutException:
            print("ERROR: Checkout overview page not found within the timeout.")
            return False

    def verify_checkout_overview(self):
        """
        Verifies that the products listed in the checkout overview match the cart contents
        and completes the checkout process.
        """
        try:
            # Fetch product details from the checkout overview page
            checkout_products = self.driver.find_elements(By.CLASS_NAME, SwagLabsLocators.cart_item_locator)
            print("\nVerifying products in the checkout overview:")

            # Check if there are no products in the checkout overview and print an error message
            if len(checkout_products) == 0:
                print("ERROR: No products found in the checkout overview.")
                return False

            # Verify each product's details
            for i, product in enumerate(checkout_products):
                name = product.find_element(By.CLASS_NAME, SwagLabsLocators.inventory_item_name_locator).text
                price = product.find_element(By.CLASS_NAME, SwagLabsLocators.inventory_item_price_locator).text
                print(f"Product {i + 1} verified: {name}, Price: {price}")

            # Click the finish button to complete the checkout
            finish_button = self.wait.until(EC.element_to_be_clickable((By.ID, SwagLabsLocators.finish_button_locator)))
            finish_button.click()

            # Wait for the confirmation page to load
            self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, SwagLabsLocators.order_confirmation_message_locator)))

            # Get the confirmation message
            confirmation_message = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, SwagLabsLocators.order_confirmation_message_locator))).text
            print(f"\nCheckout Confirmation: {confirmation_message}")
            return True

        # Handling exceptions
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print(f"ERROR during checkout: {error}")
            return False

    def shutdown(self):
        """
        Closes the WebDriver and resets the shared instance.
        """
        self.driver.quit()
        SwaglabsCheckoutPage.driver = None
        return True