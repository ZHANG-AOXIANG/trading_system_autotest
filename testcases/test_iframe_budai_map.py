# @PURPOSE:
# @AUTHOR: Aoxiang Zhang
# @TIME: 00:10 2024/5/12 UTC+8

import time

from config.WebdriverConfig import WebdriverConfig
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.IframeBaiduMapPage import IframeBaiduMapPage


class TestIframeBaiduMap:
    def test_iframe_baidu_map(self, driver):
        LoginPage().login(driver, "jay")
        time.sleep(1)
        LeftMenuPage().click_level_one_menu(driver, "iframe测试")
        time.sleep(1)
        IframeBaiduMapPage().switch_into_baidu_map_iframe(driver)
        time.sleep(1)
        IframeBaiduMapPage().get_baidu_map_search_button(driver)
        time.sleep(1)
        IframeBaiduMapPage().out_from_baidu_map_iframe(driver)
        time.sleep(1)
        LeftMenuPage().click_level_one_menu(driver, "首页")
        driver.quit()
