# @PURPOSE:
# @AUTHOR: Aoxiang Zhang
# @TIME: 23:46 2024/5/11 UTC+8


import time
from config.WebdriverConfig import WebdriverConfig
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.AccountPage import AccountPage


class TestUploadProfileImg(LoginPage, AccountPage):
    def test_upload_profile_img(self):
        driver = WebdriverConfig().webdirver_config()
        LoginPage().login(driver, "jay")
        LeftMenuPage().click_level_one_menu(driver, "账户设置")
        time.sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "个人资料")
        time.sleep(1)
        AccountPage().upload_profile_img(driver, "profile_img.jpg")
        time.sleep(2)
        AccountPage().click_save(driver)
        time.sleep(2)
        driver.quit()
