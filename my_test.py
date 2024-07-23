from seleniumbase import BaseCase
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
import time
from openpyxl import Workbook

BaseCase.main(__name__, __file__)

class MyTestClass(BaseCase):
    def test_swag_labs(self):
        self.results = []
        
        def log_result(step, status, message=""):
            self.results.append({"Step": step, "Status": status, "Message": message})
        
        self.open("https://www.saucedemo.com")
        time.sleep(2)
        log_result("Open Website", "Success")
        
        try:
            # Login
            self.type("#user-name", "standard_user")
            time.sleep(1)
            self.type("#password", "secret_sauce\n")
            time.sleep(2)
            log_result("Login", "Success")

            # Verify products list
            self.assert_element("div.inventory_list")
            self.assert_exact_text("Products", "span.title")
            time.sleep(1)
            log_result("Verify Products List", "Success")

            # Add item to cart
            self.click('button[name*="backpack"]')
            time.sleep(2)
            self.click("#shopping_cart_container a")
            time.sleep(1)
            log_result("Add Item to Cart", "Success")

            # Verify cart
            self.assert_exact_text("Your Cart", "span.title")
            self.assert_text("Backpack", "div.cart_item")
            time.sleep(2)
            log_result("Verify Cart", "Success")

            # Checkout process
            self.click("button#checkout")
            time.sleep(1)
            log_result("Checkout Process", "Success")

            # Fill checkout form
            self.type("#first-name", "SeleniumBase")
            self.type("#last-name", "Automation")
            self.type("#postal-code", "77123")
            time.sleep(2)
            self.click("input#continue")
            time.sleep(1)
            log_result("Fill Checkout Form", "Success")

            # Verify checkout overview
            self.assert_exact_text("Checkout: Overview", "span.title")
            self.assert_text("Backpack", "div.cart_item")
            self.assert_text("29.99", "div.inventory_item_price")
            time.sleep(2)
            log_result("Verify Checkout Overview", "Success")

            # Finish order
            self.click("button#finish")
            time.sleep(1)
            self.assert_exact_text("Thank you for your order!", "h2")
            time.sleep(2)
            log_result("Finish Order", "Success")

            # Logout
            try:
                BURGER_MENU_XPATH = (By.XPATH, "//button[@id='react-burger-menu-btn']")
                l = self.driver.find_element(*BURGER_MENU_XPATH)
                l.click()
                time.sleep(1)

                LOGOUT_XPATH = (By.XPATH, "//a[@id='logout_sidebar_link']")
                g = self.driver.find_element(*LOGOUT_XPATH)
                g.click()
                log_result("Logout", "Success")
            except ElementNotVisibleException:
                log_result("Logout", "Failure", "Menu button not visible")

            # Verify logout
            time.sleep(3)
            LOGIN_XPATH = (By.XPATH, "//input[@id='login-button']")
            l = self.driver.find_element(*LOGIN_XPATH)
            self.assertEqual(l.get_attribute("value"), "Login")
            time.sleep(3)
            log_result("Verify Logout", "Success")

            # Deliberately fail a step
            try:
                self.find_element("#non_existent_element")
                log_result("Find Non-Existent Element", "Failure", "Element should not be found")
            except NoSuchElementException:
                log_result("Find Non-Existent Element", "Success", "Element not found as expected")

        except Exception as e:
            log_result("Test Execution", "Failure", str(e))
        
        # Generate Excel Report
        self.generate_excel_report()

    def generate_excel_report(self):
        wb = Workbook()
        ws = wb.active
        ws.title = "Test Results"

        # Headers
        ws.append(["Step", "Status", "Message"])

        # Add data
        for result in self.results:
            ws.append([result["Step"], result["Status"], result["Message"]])

        # Save the file
        wb.save("test_results.xlsx")
