# @PURPOSE:
# @AUTHOR: Aoxiang Zhang
# @TIME: 22:56 2024/5/11 UTC+8

import time

from config.WebdriverConfig import WebdriverConfig
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.OrderPage import OrderPage


class TestSearchOrderBuy:
    def test_search_order_buy(self, driver):
        LoginPage().login(driver, "jay")
        LeftMenuPage().click_level_one_menu(driver, "我的订单")
        time.sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "已买到的宝贝")
        time.sleep(1)
        button_list = ["全部", "待付款", "待发货", "运输中", "待确认", "待评价"]
        for button in button_list:
            OrderPage().click_button_in_order_page(driver, button)
            time.sleep(2)
        driver.quit()
