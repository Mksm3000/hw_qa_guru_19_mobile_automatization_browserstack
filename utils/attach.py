import os

import allure
import requests


def png_attachment(browser):
    allure.attach(browser.driver.get_screenshot_as_png(),
                  name='screenshot',
                  attachment_type=allure.attachment_type.PNG)


def xml_attachment(browser):
    allure.attach(browser.driver.page_source,
                  name='screen xml dump',
                  attachment_type=allure.attachment_type.XML)


def video_attachment(session_id):
    bs_session = requests.get(url=f'https://api.browserstack.com/app-automate/sessions/'
                                  f'{session_id}.json',
                              auth=((os.getenv('BS_NAME'), os.getenv('BS_KEY')))).json()
    video_url = bs_session["automation_session"]["video_url"]

    allure.attach('<html><body>'
                  '<video width="100%" height="100%" controls autoplay>'
                  f'<source src="{video_url}" type="video/mp4">'
                  '</video></body></html>',
                  name='video recording',
                  attachment_type=allure.attachment_type.HTML)
