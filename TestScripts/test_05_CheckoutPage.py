"""
test_05_CheckoutPage.py
This file contains Selenium test scripts for testing the Swag Labs Checkout Page.
"""

from PageObjects.CheckoutPage import SwaglabsCheckoutPage

# Test case for starting the checkout process
def test_checkout():
    SwaglabsCheckoutPage().start()  # Initialize the browser and navigate to the checkout page
    assert SwaglabsCheckoutPage().checkout()  # Start the checkout process and verify it's successful
    print("SUCCESS: CHECKOUT STARTED!")  # Print confirmation message

# Test case for capturing a screenshot of the checkout overview page
def test_capture_screenshot():
    assert SwaglabsCheckoutPage().capture_screenshot()  # Capture a screenshot of the checkout overview page
    print("SUCCESS: SCREENSHOT CAPTURED!")  # Print confirmation message

# Test case for verifying the checkout overview and product details
def test_verify_checkout_overview():
    assert SwaglabsCheckoutPage().verify_checkout_overview()  # Verify the checkout overview and product details are correct
    print("\nSUCCESS: CHECKOUT OVERVIEW AND PRODUCT DETAILS HAVE BEEN VERIFIED, AND THEY CONTAIN THE SAME PRODUCTS AS SELECTED!")  # Print confirmation message
    SwaglabsCheckoutPage().shutdown()  # Close the browser and cleanup