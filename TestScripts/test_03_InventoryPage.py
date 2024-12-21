"""
test_03_InventoryPage.py
This file contains Selenium test scripts for testing the Swag Labs Inventory Page.
"""

from PageObjects.InventoryPage import SwagLabsInventoryPage

# Test case for selecting 4 random products
def test_get_random_products():
    SwagLabsInventoryPage().start()  # Initialize the browser and open the inventory page
    assert SwagLabsInventoryPage().get_random_products()  # Select 4 random products and verify the operation
    SwagLabsInventoryPage().shutdown()  # Close the browser and cleanup
    print("SUCCESS: RANDOMLY 4 PRODUCTS SELECTED !")  # Print confirmation message