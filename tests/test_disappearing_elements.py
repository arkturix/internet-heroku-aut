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
    for elem in menu_item_elems:
        assert elem.is_displayed(), f"The {elem.text} menu item was not displayed."

    logger.info("Check that all menu items are available")
    assert [elem.text for elem in menu_item_elems] == variables['disappearing_elements_menu_list']