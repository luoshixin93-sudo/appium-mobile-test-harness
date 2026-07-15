from appium.webdriver.common.appiumby import AppiumBy
from utils.common import get_logger

logger = get_logger()


class HomePage:
    """Page Object for the Home screen."""

    def __init__(self, driver):
        self.driver = driver
        self.home_title = (AppiumBy.ID, "com.example:id/homeTitle")
        self.logout_button = (AppiumBy.ACCESSIBILITY_ID, "logoutBtn")

    def is_home_page_displayed(self):
        try:
            el = self.driver.find_element(*self.home_title)
            return el.is_displayed()
        except Exception:
            return False

    def get_title(self):
        try:
            el = self.driver.find_element(*self.home_title)
            return el.text
        except Exception:
            return None
