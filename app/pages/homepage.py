from selenium.webdriver.common.by import By


class Homepage:

    def __init__(self, driver):
        """initialize homepage object"""
        self.driver = driver
        self.cart_nav_link = "a[href='/cart']"

    def check_cart_items(self):
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.cart_nav_link).click()
