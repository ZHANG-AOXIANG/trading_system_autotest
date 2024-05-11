# @PURPOSE:
# @AUTHOR: Aoxiang Zhang
# @TIME: 22:52 2024/5/11 UTC+8

from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.OrderBase import OrderBase


class OrderPage(ObjectMap, OrderBase):

    def click_button_in_order_page(self, driver, button_name):
        """
        click the button in order page
        :param driver: driver's browser
        :param button_name: button's name
        return
        """
        button_xpath = self.order_tab_button_xpath(button_name)
        return self.element_click(driver, By.XPATH, button_xpath)
