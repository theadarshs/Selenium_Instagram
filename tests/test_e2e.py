import time
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.loginPage import LoginPage
from utilities.BaseClass import BaseClass
from selenium.webdriver.support import expected_conditions as EC


class TestInstagramLogin(BaseClass):

    def test_login(self):
        log = self.getLogger()

        # Create LoginPage object
        login_page = LoginPage(self.driver)
        time.sleep(5)
        #Set username and password
        login_page.set_username().send_keys("your username")
        login_page.set_password().send_keys("your password")

        #Click on Login button
        login_page.click_login_button()
        time.sleep(15)
        # Wait for the title to contain "Instagram"
        #WebDriverWait(self.driver, 10).until(EC.title_contains('Instagram'))
        # Check if there is an error message
        error_message = login_page.get_error_message()
        if error_message == "Sorry, your password was incorrect. Please double-check your password.":
            log.error(error_message)
        else:
            log.info('Logged in successfully')