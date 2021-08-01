import pytest
from herokuapp_internet.login_page import LoginPage
from herokuapp_internet.disappearing_elements_page import DisappearingElementsPage
import logging

logger = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def login_page():
    login = LoginPage()
    yield login

    login.quit()


@pytest.fixture(scope="module")
def de_page():
    dissapearing_elems = DisappearingElementsPage()
    yield dissapearing_elems

    dissapearing_elems.quit()
