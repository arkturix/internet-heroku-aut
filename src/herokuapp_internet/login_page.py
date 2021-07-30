from .browser import Browser
import logging

logger = logging.getLogger(__name__)


class LoginPage(Browser):
    def __init__(self, **kwargs):
        self._url = "http://the-internet.herokuapp.com/login"
        super().__init__(**kwargs)
        self.get_page(self._url)

    def action_is_successful(self) -> bool:
        """Determine if an action is succesfful based on presence of success banner"""
        success_banner_elem = self.driver.find_element_by_css_selector("#flash.flash.success")
        return success_banner_elem.is_displayed()

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

    def login_success(self):
        """Determine if login is successful"""
        return self.action_is_successful()

    def login_success_message(self):
        success_banner_elem = self.driver.find_element_by_css_selector("#flash.flash.success")
        if success_banner_elem.is_displayed():
            logger.debug(f"Success message displayed: {success_banner_elem.text}")
            return success_banner_elem.text
        return None

    def get_error_message(self):
        """Get error message on failure"""
        error_banner_elem = self.driver.find_element_by_id("#flash.flash.error")
        if error_banner_elem.is_displayed():
            logger.debug(f"Error message displayed: {error_banner_elem.text}")
            return error_banner_elem.text
        logger.debug("No error displayed")
        return None

    def click_logout_button(self):
        """Click on the logout button"""
        logger.debug("Clicking the logout button")
        self.driver.find_element_by_css_selector('a.button.secondary.radius').click()

    def logout_success(self):
        """Determine if logout is successful"""
        return self.action_is_successful()
