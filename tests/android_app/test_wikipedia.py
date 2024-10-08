from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_search():

    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID,
                         'org.wikipedia.alpha:id/search_src_text')).type('Apple')

    with (step('Verify content found')):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))

    with step('Click on "Apple Inc."'):
        results.element_by(have.text('Apple Inc.')).click()

