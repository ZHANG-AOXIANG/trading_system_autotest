# @PURPOSE:
# @AUTHOR: Aoxiang Zhang
# @TIME: 22:58 2024/5/9 UTC+8
import time

from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.GoodsBase import GoodsBase
from common.tools import get_img_path


class GoodsPage(ObjectMap, GoodsBase):
    def input_goods_title(self, driver, goods_title: str):
        """
        Input goods titile
        :param goods_title: goods' title
        """
        goods_title_xpath = self.goods_title_xpath()
        return self.fill_value(driver, By.XPATH, goods_title_xpath, goods_title)

    def input_goods_details(self, driver, goods_details: str):
        """
        Input goods details
        :param goods_details: goods' details
        """
        goods_details_xpath = self.goods_detail_xpath()
        return self.fill_value(driver, By.XPATH, goods_details_xpath, goods_details)

    def select_goods_num(self, driver, goods_num):
        """
        select goods num
        :param goods_num: goods' num
        """
        goods_num_input_box_xpath = self.goods_num_input_xpath()
        return self.fill_value(driver, By.XPATH, goods_num_input_box_xpath, goods_num)

    def upload_goods_img(self, driver, img_name):
        """
        upload good's image
        :param driver: browser's driver
        :param img_name: image's name
        """
        img_path = get_img_path(img_name)
        upload_img_xpath = self.goods_img_xpath()
        return self.upload_file(driver, By.XPATH, upload_img_xpath, img_path)

    def input_goods_price(self, driver, goods_price):
        """
        input goods price
        :param driver: browser's driver
        :param goods_price: goods' price
        """
        goods_price_xpath = self.goods_price_xpath()
        return self.fill_value(driver, By.XPATH, goods_price_xpath, goods_price)

    def select_goods_status(self, driver, goods_status):
        """
        select goods' status
        :param driver: broswer's driver
        :param goods_status: goods' status
        """
        goods_status_xpath = self.goods_status_xpath()
        self.element_click(driver, By.XPATH, goods_status_xpath)
        time.sleep(1)
        goods_status_select_xpath = self.select_goods_status_xpath(goods_status)
        return self.element_click(driver, By.XPATH, goods_status_select_xpath)

    def click_bottom_button(self, driver, button_name):
        """
        click the button at goods page buttom
        :param driver: browser's driver
        :param button_name: "提交", "重置"
        """
        button_xpath = self.button_goods_page_bottom_xpath(button_name)
        return self.element_click(driver, By.XPATH, button_xpath)

    def add_new_goods(
            self,
            driver,
            goods_title,
            goods_detail,
            goods_num,
            goods_img_path,
            goods_price,
            goods_status,
            button_name="提交"
    ):
        """
        add a new goods
        :param driver: browser's driver
        :param goods_title: goods' title
        :param goods_detail: goods' detail
        :param goods_num: goods' number
        :param goods_img_path: goods image's path
        :param goods_price: goods' price
        :param goods_status: goods' status
        """
        self.input_goods_title(driver, goods_title)
        time.sleep(0.5)
        self.input_goods_details(driver, goods_detail)
        time.sleep(0.5)
        self.select_goods_num(driver, goods_num)
        time.sleep(0.5)
        self.upload_goods_img(driver, goods_img_path)
        time.sleep(0.5)
        self.input_goods_price(driver, goods_price)
        time.sleep(0.5)
        self.select_goods_status(driver, goods_status)
        self.click_bottom_button(driver, button_name=button_name)
