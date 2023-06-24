from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    USERNAME_INPUT = (By.NAME, 'username')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    ERROR_MSG = (By.ID, 'slfErrorAlert')

    def set_username(self):
        return self.driver.find_element(*LoginPage.USERNAME_INPUT)

    def set_password(self):
        return self.driver.find_element(*LoginPage.PASSWORD_INPUT)

    def click_login_button(self):
        self.driver.find_element(*LoginPage.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.driver.find_element(*LoginPage.ERROR_MSG).text
