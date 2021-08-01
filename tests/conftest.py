import pytest
from herokuapp_internet.login_page import LoginPage
from herokuapp_internet.disappearing_elements_page import DisappearingElementsPage
import logging

logger = logging.getLogger(__name__)


def pytest_addoption(parser):
    parser.addoption(
        "--headless", action="store", default="false", help="Run browser tests in headless mode. Default: false"
    )


@pytest.fixture(scope='session')
def headless_option(request):
    if request.config.getoption("--headless") == "false":
        return False
    else:
        return True


@pytest.fixture(scope="module")
def login_page(headless_option):
    login = LoginPage(headless=headless_option)
    yield login

    login.quit()


@pytest.fixture(scope="module")
def de_page(headless_option):
    dissapearing_elems = DisappearingElementsPage(headless=headless_option)
    yield dissapearing_elems

    dissapearing_elems.quit()
