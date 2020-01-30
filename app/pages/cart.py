from selenium.webdriver.common.by import By


class Cart:

    def __init__(self, driver):
        self.driver = driver
        self.cart_contents = ".shopping-cart div.content"

    def cart_items_text(self):
        cart_contents = self.driver.find_element(by=By.CSS_SELECTOR, value=self.cart_contents)
        return cart_contents.text
