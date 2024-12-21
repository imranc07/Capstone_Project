"""
test_04_CartPage.py
This file contains Selenium test scripts for testing the Swag Labs Cart Page.
"""

from PageObjects.CartPage import SwagLabsCartPage

# Test case for verifying cart button is visible or not
def test_is_cart_button_visible():
    SwagLabsCartPage().start()  # Initialize the browser and open the cart page
    assert SwagLabsCartPage().is_cart_button_visible()  # Verifies cart button visibility
    print("SUCCESS: CART BUTTON VISIBILITY VERIFIED!")  # Print confirmation message
    SwagLabsCartPage().shutdown()  # Close the browser and cleanup

# Test case for adding selected products to the cart
def test_add_to_cart():
    SwagLabsCartPage().start()  # Initialize the browser and open the cart page
    assert SwagLabsCartPage().add_to_cart()  # Add randomly selected products to the cart
    print("SUCCESS: RANDOMLY 4 PRODUCTS ADDED TO CART!")  # Print confirmation message

# Test case to verify the cart badge count
def test_verify_cart_badge():
    assert SwagLabsCartPage().verify_cart_badge()  # Verify the cart badge displays the correct number of items
    print("SUCCESS: CART BADGE VERIFIED!")  # Print confirmation message

# Test case to verify product details in the cart page
def test_verify_cart_page():
    assert SwagLabsCartPage().verify_cart_page()  # Check that the cart contains the same products as selected
    print("SUCCESS: THE CART PAGE HAS BEEN VERIFIED, AND IT CONTAINS THE SAME PRODUCTS AS SELECTED!")  # Print confirmation message
    SwagLabsCartPage().shutdown()  # Close the browser and cleanup