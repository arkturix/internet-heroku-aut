from .browser import Browser
import logging

logger = logging.getLogger(__name__)


class Login(Browser):
    def __init__(self, **kwargs):
        self._url = "http://the-internet.herokuapp.com/login"
        super().__init__(**kwargs)
        self.get_page(self._url)

    def fill_username(self, username):
        pass

    def fill_password(self, password):
        pass

    def click_login_button(self):
        pass

    def get_error_message(self):
        pass
