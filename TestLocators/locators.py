"""
locators.py
This file contains all the locators used for interacting with elements on the Swag Labs application.
"""

class SwagLabsLocators:
    # Locators for Login Page
    username_locator = 'user-name'  # ID locator for the username input field
    password_locator = 'password'  # ID locator for the password input field
    login_button_locator = 'login-button'  # ID locator for the login button
    menu_button_locator = 'react-burger-menu-btn'  # ID locator for the menu button
    logout_button_locator = 'logout_sidebar_link'  # ID locator for the logout dropdown

    # Locators for Inventory Page
    inventory_item_locator = 'inventory_item'  # Class Name locator for inventory items
    inventory_item_name_locator = 'inventory_item_name'  # Class Name locator for inventory item names
    inventory_item_price_locator = 'inventory_item_price'  # Class Name locator for inventory item prices
    add_to_cart_button_locator = 'btn_inventory'  # Class Name locator for the "Add to Cart" button
    cart_badge_locator = 'shopping_cart_badge'  # Class Name locator for the cart badge

    # Locators for Cart Page
    cart_link_locator = 'shopping_cart_link'  # Class Name locator for the cart link
    cart_list_locator = 'cart_list'  # Class Name locator for the list of items in the cart
    cart_item_locator = 'cart_item'  # Class Name locator for individual cart items
    checkout_button_locator = 'checkout'  # ID locator for the "Checkout" button

    # Locators for Checkout Page
    first_name_locator = 'first-name'  # ID locator for the first name input box
    last_name_locator = 'last-name'  # ID locator for the last name input box
    postal_code_locator = 'postal-code'  # ID locator for the postal code input box
    continue_button = 'continue'  # ID locator for the "Continue" button
    checkout_summary_locator = 'checkout_summary_container'  # ID locator for the checkout summary section
    finish_button_locator = 'finish'  # ID locator for the "Finish" button
    order_confirmation_message_locator = 'complete-header'  # Class Name locator for the order confirmation message