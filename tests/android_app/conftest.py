import os

import pytest
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from selene import browser


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def mobile_management():

    options = UiAutomator2Options().load_capabilities({

        # "platformName": "android", # default value
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        "app": "bs://sample.app",

        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            "userName": os.getenv('BS_NAME'),
            "accessKey": os.getenv('BS_KEY')
        }
    })

    browser.config.driver_remote_url = 'http://hub.browserstack.com/wd/hub'
    browser.config.driver_options = options

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    browser.config._wait_decorator

    yield

    browser.quit()
