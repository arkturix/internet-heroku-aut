from .browser import Browser
import logging

logger = logging.getLogger(__name__)


class DisappearingElementsPage(Browser):
    def __init__(self, **kwargs):
        self.url = "http://the-internet.herokuapp.com/disappearing_elements"
        super().__init__(**kwargs)
        self.go_to_page()

    def go_to_page(self):
        """Go to the Disappearing Elements page"""
        self.get_page(self.url)
