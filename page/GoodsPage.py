# @PURPOSE:
# @AUTHOR: Aoxiang Zhang
# @TIME: 22:58 2024/5/9 UTC+8
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
        goods_title_xpath = self.goods_title_xpath(goods_title)
        return self.fill_value(driver, By.XPATH, goods_title_xpath, goods_title)

    def input_goods_details(self, driver, goods_details: str):
        """
        Input goods details
        :param goods_details: goods' details
        """
        goods_details_xpath = self.goods_detail_xpath()
        return self.fill_value(driver, By.XPATH, goods_details_xpath, goods_details)
