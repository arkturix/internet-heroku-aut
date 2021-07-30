import pytest
import logging

logger = logging.getLogger(__name__)

smoke = pytest.mark.smoke


@smoke
def test_login_and_logout(login_page, variables):
    logger.info("Test logging in and logging out")
    login_page.go_to_page()
    login_page.fill_username(variables["login_page"]["username"])
    login_page.fill_password(variables["login_page"]["password"])
    login_page.click_login_button()
    logger.info("Logging in...")
    login_page.take_screenshot()
    assert login_page.login_sucess(), "Login failed"

    logger.info("Login successful, logging out...")
    login_page.click_logout_button()
    login_page.take_screenshot()
    assert login_page.logout_success()


@smoke
def test_bad_username(login_page, variables):
    logger.info("Test login with bad username")
    login_page.go_to_page()
    login_page.fill_username(variables["login_page"]["bad_username"])
    login_page.fill_password(variables["login_page"]["password"])
    login_page.click_login_button()
    login_page.take_screenshot()
    assert login_page.login_failure()

    logger.info("Login failed")
    login_error = login_page.get_error_message()
    assert (
        login_error == "Your username is invalid!"
    ), f"Error message is incorrect: {login_error}"


@smoke
def test_bad_password(login_page, variables):
    logger.info("Test login with bad password")
    login_page.go_to_page()
    login_page.fill_username(variables["login_page"]["username"])
    login_page.fill_password(variables["login_page"]["bad_password"])
    login_page.click_login_button()
    login_page.take_screenshot()
    assert login_page.login_failure()

    logger.info("Login failed")
    login_error = login_page.get_error_message()
    assert (
        login_error == "Your password is invalid!"
    ), f"Error message is incorrect: {login_error}"
