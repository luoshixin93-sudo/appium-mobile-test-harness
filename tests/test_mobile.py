import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.common import get_logger, get_test_data, read_date, read_time

logger = get_logger()


@pytest.mark.regression
class TestMobileApp:
    """Mobile app automation test suite using Appium + POM."""

    @pytest.fixture(autouse=True)
    def setup(self, appium_driver):
        self.driver = appium_driver
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        logger.info("Test fixture setup complete")

    def test_login_with_valid_credentials(self):
        """Test successful login with valid user credentials."""
        logger.info("Starting test: valid login")
        test_data = get_test_data("login_valid")[0]
        self.login_page.enter_username(test_data["username"])
        self.login_page.enter_password(test_data["password"])
        self.login_page.click_login()
        assert self.home_page.is_home_page_displayed(), "Home page not displayed after login"
        logger.info("Valid login test passed")

    def test_login_with_invalid_credentials(self):
        """Test login failure with invalid credentials."""
        logger.info("Starting test: invalid login")
        test_data = get_test_data("login_invalid")[0]
        self.login_page.enter_username(test_data["username"])
        self.login_page.enter_password(test_data["password"])
        self.login_page.click_login()
        assert self.login_page.is_error_message_displayed(), "Error message not shown for invalid login"
        logger.info("Invalid login test passed")

    def test_home_page_elements(self):
        """Verify all key UI elements are present on the home page."""
        self.login_page.enter_username("testuser")
        self.login_page.enter_password("password")
        self.login_page.click_login()
        assert self.home_page.is_home_page_displayed()
        assert self.home_page.get_title() is not None
        logger.info("Home page elements verified")
