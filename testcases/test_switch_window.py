# @PURPOSE:
# @AUTHOR: Aoxiang Zhang
# @TIME: 22:31 2024/5/11 UTC+8

import time
from config.WebdriverConfig import WebdriverConfig
from page.ExternalLinkPage import ExternalLinkPage
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage


class TestSwitchWindow:
    def test_switch_window(self):
        driver = WebdriverConfig().webdirver_config()
        LoginPage().login(driver, "jay")
        time.sleep(3)
        LeftMenuPage().click_level_one_menu(driver, "外链")
        time.sleep(1)
        title = ExternalLinkPage().goto_imooc(driver)
        print(title)
        driver.quit()
