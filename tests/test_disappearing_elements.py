import pytest
import logging

logger = logging.getLogger(__name__)

smoke = pytest.mark.smoke


@smoke
def test_menu_items_visible(de_page, variables):
    logger.info("Testing all menu items visible")
    de_page.go_to_page()
    menu_item_elems = de_page.get_menu_items()
    logger.debug('Check that all menu elements retrieved are displayed.')
    assert all([elem.is_displayed() for elem in menu_item_elems]), "One or more menu items that exist are not displayed"

    logger.info("Check that all menu items are available")
    assert variables['disappearing_elements_menu_list'] == [elem.text for elem in menu_item_elems], "The expected menu items (left) did not match the existing menu items (right)"