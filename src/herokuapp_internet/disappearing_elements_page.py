from .browser import Browser
import logging

logger = logging.getLogger(__name__)


class DisappearingElementsPage(Browser):
    def __init__(self, **kwargs):
        self._url = "http://the-internet.herokuapp.com/disappearing_elements"
        super().__init__(**kwargs)
        self.get_page(self._url)

    
