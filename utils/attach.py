import os

import allure
import requests


def png_attachment(browser):
    allure.attach(browser.driver.get_screenshot_as_png(),
                  name='screenshot',
                  attachment_type=allure.attachment_type.PNG)


def xml_attachment(browser):
    allure.attach(source=browser.driver.page_source,
                  name='screen xml dump',
                  attachment_type=allure.attachment_type.XML,
                  extension='.xml')


def log_attachment(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(source=log,
                  name='browser_logs',
                  attachment_type=allure.attachment_type.TEXT,
                  extension='.log')


def html_attachment(browser):
    html = browser.driver.page_source
    allure.attach(source=html,
                  name='page_source',
                  attachment_type=allure.attachment_type.HTML,
                  extension='.html')


def web_video_attachment(browser):
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(source=html,
                  name='video_' + browser.driver.session_id,
                  attachment_type=allure.attachment_type.HTML,
                  extension='.html')


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
