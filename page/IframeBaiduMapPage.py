# @PURPOSE:
# @AUTHOR: Aoxiang Zhang
# @TIME: 00:08 2024/5/12 UTC+8

from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.IframeBaiduMapBase import IframeBaiduMapBase


class IframeBaiduMapPage(ObjectMap, IframeBaiduMapBase):
    def get_baidu_map_search_button(self, driver):
        """
        get the element of search button in baidu map iframe
        :param driver: browser's driver
        """
        button_xpath = self.search_button_xpath()
        return self.get_element(driver, By.XPATH, button_xpath)

    def switch_into_baidu_map_iframe(self, driver):
        """
        switch into baidu map iframe
        :param driver: browser's driver
        """
        iframe_xpath = self.baidu_map_iframe_xpath()
        return self.into_iframe(driver, By.XPATH, iframe_xpath)

    def out_from_baidu_map_iframe(self, driver):
        """
        switch out from baidu map iframe
        :param driver: browser's driver
        """
        return self.out_from_iframe(driver)
