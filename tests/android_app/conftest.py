import os

import allure
import allure_commons
import pytest
import requests
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from selene import browser, support
from appium import webdriver

import config
from utils.attach import video_attachment, png_attachment, xml_attachment


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({

        # 'platformName': 'android', # default value
        'platformVersion': config.platformVersion,
        'deviceName': config.deviceName,

        'app': config.app,

        'bstack:options': {
            'projectName': 'First Python project',
            'buildName': 'browserstack-build-1',
            'sessionName': 'BStack first_test',

            'userName': os.getenv('BS_NAME'),
            'accessKey': os.getenv('BS_KEY')
        }
    })

    # browser.config.driver_remote_url = 'http://hub.browserstack.com/wd/hub'
    # browser.config.driver_options = options

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            'http://hub.browserstack.com/wd/hub',
            options=options)

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext)

    yield

    png_attachment(browser)

    xml_attachment(browser)

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    video_attachment(session_id)
