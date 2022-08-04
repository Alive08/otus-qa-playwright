import datetime
import time

import allure
from allure_commons.types import AttachmentType
from playwright.sync_api import Page


def take_screenshot_playwright(page: Page, dir, nodeid):
    time.sleep(1)
    file_name = f'{nodeid}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace("/",
                                                                                      "_").replace("::", "__")

    with open(f"{dir}/{file_name}", 'wb') as bin_file:
        bin_file.write(page.screenshot(full_page=True))

    return file_name


def take_screenshot_allure(page: Page, nodeid):
    # time.sleep(1)
    allure.attach(page.screenshot(full_page=True, type='png'), name=nodeid,
                  attachment_type=AttachmentType.PNG)
