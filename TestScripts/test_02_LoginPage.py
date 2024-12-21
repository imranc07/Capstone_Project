"""
test_02_LoginPage.py
This file contains Selenium test scripts for testing the Swag Labs Login Page.
"""

from PageObjects.LoginPage import SwagLabsLoginPage

# Test case for verifying the login functionality
def test_login():
    SwagLabsLoginPage().start()  # Start the browser and navigate to the login page
    assert SwagLabsLoginPage().login()  # Attempt to log in and check if successful
    print("SUCCESS: LOGGED IN!")  # Print success message if login is successful

# Test case to check if the logout button is visible after login
def test_is_logout_button_visible():
    assert SwagLabsLoginPage().is_logout_button_visible()  # Verify if the logout button is visible
    print("SUCCESS: LOGOUT BUTTON IS VISIBLE")  # Print success message if the button is visible

# Test case for verifying the logout functionality
def test_logout():
    assert SwagLabsLoginPage().logout()  # Attempt to log out and check if successful
    SwagLabsLoginPage().shutdown()  # Close the browser and cleanup
    print("SUCCESS: LOGGED OUT!")  # Print success message if logout is successful