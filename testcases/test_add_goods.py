# @PURPOSE:
# @AUTHOR: Aoxiang Zhang
# @TIME: 21:25 2024/5/10 UTC+8
import time

import pytest

from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.GoodsPage import GoodsPage

goods_info_list = [
    {
        "goods_title": "book",
        "goods_detail": "计算机与人脑",
        "goods_num": 2,
        "goods_img_path": "book.jpg",
        "goods_price": 20,
        "goods_status": "上架"
    },
    {
        "goods_title": "test-title-2",
        "goods_detail": "test-detail-2",
        "goods_num": 2,
        "goods_img_path": "book.jpg",
        "goods_price": 10,
        "goods_status": "上架"
    }
]


class TestAddGoods:
    @pytest.mark.parametrize("goods_info", goods_info_list)
    def test_add_goods_001(self, driver, goods_info):
        LoginPage().login(driver, "jay")
        LeftMenuPage().click_level_one_menu(driver, "产品")
        time.sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "新增二手商品")
        time.sleep(2)
        GoodsPage().add_new_goods(
            driver,
            goods_title=goods_info["good_title"],
            goods_detail=goods_info["goods_detail"],
            goods_num=goods_info["goods_num"],
            goods_img_path=goods_info["goods_img_path"],
            goods_price=["goods_price"],
            goods_status=["goods_status"]
        )
        time.sleep(20)


"""
class TestAddGoods:

    def test_add_goods_001(self, driver):
        # driver = WebdriverConfig().webdirver_config()
        LoginPage().login(driver, "jay")
        LeftMenuPage().click_level_one_menu(driver, "产品")
        time.sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "新增二手商品")
        time.sleep(2)

        GoodsPage().add_new_goods(driver, goods_title="book", goods_detail="计算机与人脑", goods_num=2,
                                  goods_img_path="book.jpg", goods_price=20, goods_status="上架"
                                  )
        time.sleep(20)
"""
