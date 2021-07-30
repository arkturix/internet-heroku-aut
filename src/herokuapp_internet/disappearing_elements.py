from .browser import Browser
import logging

logger = logging.getLogger(__name__)


class DisappearingElements(Browser):
    def __init__(self, **kwargs):
        self._url = "http://the-internet.herokuapp.com/disappearing_elements"
        super().__init__(**kwargs)
