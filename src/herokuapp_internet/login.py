from .browser import Browser
import logging

logger = logging.getLogger(__name__)


class Login(Browser):
    def __init__(self, **kwargs):
        self._url = "http://the-internet.herokuapp.com/login"
        super().__init__(**kwargs)
