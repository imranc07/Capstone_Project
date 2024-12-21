"""
data.py is used to store constant data values required for testing the Swag Labs webpage.

The class `SwagLabsData` acts as a central repository for storing:
- URLs used in the tests (e.g., login page, dashboard).
- File path of the Excel file that contains test data for data-driven testing.
- The sheet name or index of the Excel sheet containing the relevant test data.
_ User details for checkout.
"""

class SwagLabsData:

    # URL for the Swag Labs login page
    login_url = "https://www.saucedemo.com/"

    # Path to the Excel file containing the test data
    excel_file = "F:\\Python-Selenium\\VScode\\GUVI_&_Tasks\\PAT Capstone Project\\TestData\\testdata.xlsx"
    
    # Name or index of the sheet within the Excel file containing test data
    sheet_number = "TestLog"

    # Usernam and Password
    username = 'standard_user'
    password = 'secret_sauce'

    # User details for checkout
    first_name = 'Lara '
    last_name = 'Croft'
    postal_code = '9211'