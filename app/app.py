from selenium import webdriver
from app.pages.homepage import Homepage
from app.pages.cart import Cart


class App:

    def __init__(self):
        chrome_driver_path = '/Users/adeoke/automation_web_drivers/bin/chromedriver_79'
        driver = webdriver.Chrome(executable_path=chrome_driver_path)
        driver.implicitly_wait(20)
        app_url = 'https://traxxas.com/'
        self.driver = driver
        self.driver.get(app_url)

    def homepage(self):
        return Homepage(self.driver)

    def cart(self):
        return Cart(self.driver)
