# Selenium Testing Project

This project contains automated tests for the [Swag Labs](https://www.saucedemo.com) website using SeleniumBase, a framework built on top of Selenium WebDriver. The tests perform various actions such as logging in, adding items to the cart, and checking out. The results are logged and exported to an Excel file.

## Table of Contents

- [Project Description](#project-description)
- [Setup](#setup)
- [Usage](#usage)
- [Test Details](#test-details)
- [Generating the Excel Report](#generating-the-excel-report)
- [Contributing](#contributing)
- [License](#license)

## Project Description

This project automates the testing of the Swag Labs website using SeleniumBase. It includes:
- Logging into the website
- Verifying the product list
- Adding an item to the cart
- Checking out
- Verifying the checkout process
- Logging out
- Generating an Excel report of the test results

## Setup

### Prerequisites

- Python 3.x
- Pip
- Git

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/selenium-testing.git
   cd selenium-testing
Create a virtual environment and activate it:

sh
`python -m venv venv`
`.\venv\Scripts\activate`  
# On Windows
`source venv/bin/activate`  
# On macOS/Linux
## Install the dependencies:

`pip install -r requirements.txt`
## Dependencies
- SeleniumBase
- Openpyxl
## To install the dependencies manually:

`pip install seleniumbase openpyxl`
- Usage
## To run the tests, use the following command:
`pytest my_test_class.py`
## The MyTestClass includes the following test steps:

- Open the Swag Labs website
- Login with valid credentials
- Verify the products list
- Add a backpack to the cart
- Verify the cart
- Proceed to checkout
- Fill in checkout information
- Verify the checkout overview
- Complete the order
- Logout
- Verify logout
- Attempt to find a non-existent element to demonstrate error handling
- Generating the Excel Report
- After running the tests, an Excel report will be generated with the results. The report will be saved as test_results.xlsx in the project directory.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## Fork the Project
Create your Feature Branch (git checkout -b feature/YourFeature)
Commit your Changes (git commit -m 'Add some feature')
Push to the Branch (git push origin feature/YourFeature)
Open a Pull Request
