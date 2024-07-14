from seleniumbase import BaseCase
from selenium.common.exceptions import ElementNotVisibleException
from seleniumbase.fixtures.page_actions import wait_for_element_visible
import time

BaseCase.main(__name__, __file__)

class MyTestClass(BaseCase):
    def test_swag_labs(self):
        self.open("https://www.saucedemo.com")
        time.sleep(2)  # Adding a delay of 2 seconds after opening the website

        # Login
        self.type("#user-name", "standard_user")
        time.sleep(1)  # Adding a delay of 1 second after typing username
        self.type("#password", "secret_sauce\n")
        time.sleep(2)  # Adding a delay of 2 seconds after typing password and hitting Enter

        # Verify products list
        self.assert_element_present("div.inventory_list")
        self.assert_exact_text("Products", "span.title")
        time.sleep(1)  # Adding a delay of 1 second after asserting text

        # Add item to cart
        self.click('button[name*="backpack"]')
        time.sleep(2)  # Adding a delay of 2 seconds after clicking on the backpack button
        self.click("#shopping_cart_container a")
        time.sleep(1)  # Adding a delay of 1 second after clicking on the shopping cart link

        # Verify cart
        self.assert_exact_text("Your Cart", "span.title")
        self.assert_text("Backpack", "div.cart_item")
        time.sleep(2)  # Adding a delay of 2 seconds after asserting text

        # Checkout process
        self.click("button#checkout")
        time.sleep(1)  # Adding a delay of 1 second after clicking on the checkout button

        # Fill checkout form
        self.type("#first-name", "SeleniumBase")
        self.type("#last-name", "Automation")
        self.type("#postal-code", "77123")
        time.sleep(2)  # Adding a delay of 2 seconds after typing in the checkout form
        self.click("input#continue")
        time.sleep(1)  # Adding a delay of 1 second after clicking on the continue button

        # Verify checkout overview
        self.assert_text("Checkout: Overview")
        self.assert_text("Backpack", "div.cart_item")
        self.assert_text("29.99", "div.inventory_item_price")
        time.sleep(2)  # Adding a delay of 2 seconds after asserting text

        # Finish order
        self.click("button#finish")
        time.sleep(1)  # Adding a delay of 1 second after clicking on the finish button
        self.assert_exact_text("Thank you for your order!", "h2")
        time.sleep(2)  # Adding a delay of 2 seconds after asserting text

        # Logout
        try:
            wait_for_element_visible(self.driver, 'a#logout_sidebar_link', timeout=10)
            self.scroll_to('a#logout_sidebar_link')
            self.click("a#logout_sidebar_link")
        except ElementNotVisibleException:
            print("Element 'a#logout_sidebar_link' is still not visible after waiting.")
            # Handle the exception as per your test scenario.

        # Verify logout
        self.assert_element_present("div#login_button_container")
