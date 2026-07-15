from appium.webdriver.common.appiumby import AppiumBy
from utils.common import get_logger

logger = get_logger()


class LoginPage:
    """Page Object for the Login screen."""

    def __init__(self, driver):
        self.driver = driver
        self.username_field = (AppiumBy.ACCESSIBILITY_ID, "username")
        self.password_field = (AppiumBy.ACCESSIBILITY_ID, "password")
        self.login_button = (AppiumBy.ACCESSIBILITY_ID, "loginBtn")
        self.error_message = (AppiumBy.ID, "com.example:id/errorText")

    def enter_username(self, username):
        el = self.driver.find_element(*self.username_field)
        el.clear()
        el.send_keys(username)
        logger.info(f"Entered username: {username}")

    def enter_password(self, password):
        el = self.driver.find_element(*self.password_field)
        el.clear()
        el.send_keys(password)
        logger.info("Entered password")

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
        logger.info("Clicked login button")

    def is_error_message_displayed(self):
        try:
            el = self.driver.find_element(*self.error_message)
            return el.is_displayed()
        except Exception:
            return False
