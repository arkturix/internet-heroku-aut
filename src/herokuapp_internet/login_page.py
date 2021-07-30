from .browser import Browser
import logging

logger = logging.getLogger(__name__)


class LoginPage(Browser):
    def __init__(self, **kwargs):
        self._url = "http://the-internet.herokuapp.com/login"
        super().__init__(**kwargs)
        self.get_page(self._url)

    def fill_username(self, username: str):
        """Clear and fill the username field"""
        username_elem = self.driver.find_element_by_id("username")
        username_elem.clear()
        logger.debug(f"Sending {username} to username input field")
        username_elem.send_keys(username)
        return self

    def fill_password(self, password: str):
        """Clear and fill the password field"""
        password_elem = self.driver.find_element_by_id("password")
        password_elem.clear()
        logger.debug(f"Sending {password} to password input field")
        password_elem.send_keys(password)
        return self

    def click_login_button(self):
        """Click on login button"""
        logger.debug("Clicking login button")
        self.driver.find_element_by_css_selector(".radius").click()

    def get_error_message(self):
        """Get error message on failure"""
        error_elem = self.driver.find_element_by_id("flash")
        if error_elem.is_displayed():
            logger.debug(f"Error message displayed: {error_elem.text}")
            return error_elem.text
        logger.debug("No error displayed")
        return None
