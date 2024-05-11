# @PURPOSE:
# @AUTHOR: Aoxiang Zhang
# @TIME: 21:25 2024/5/10 UTC+8
import time

from config.WebdriverConfig import WebdriverConfig
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.GoodsPage import GoodsPage


class TestAddGoods:
    def test_add_goods_001(self):
        driver = WebdriverConfig().webdirver_config()
        LoginPage().login(driver, "jay")
        LeftMenuPage().click_level_one_menu(driver, "产品")
        time.sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "新增二手商品")
        time.sleep(2)

        GoodsPage().add_new_goods(driver, goods_title="book", goods_detail="计算机与人脑", goods_num=2,
                                  goods_img_path="book.jpg", goods_price=20, goods_status="上架"
                                  )
        time.sleep(20)
