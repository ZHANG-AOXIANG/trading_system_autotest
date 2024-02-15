# @PURPOSE:
# @AUTHOR: Aoxiang Zhang
# @TIME: 21:11 2024/2/4 UTC+8

from time import sleep

from config.WebdriverConfig import WebdriverConfig
from page.LoginPage import LoginPage


class TestLogin:
    SECONDE_ONE = 1
    SECONDE_THREE = 3

    def test_login(self):
        driver = WebdriverConfig().webdirver_config()
        driver.get("http://192.168.0.119")
        sleep(self.SECONDE_THREE)
        LoginPage().login_input_value(driver, "用户名", "周杰伦")
        sleep(self.SECONDE_ONE)
        LoginPage().login_input_value(driver, "密码", '123456')
        sleep(self.SECONDE_ONE)
        LoginPage().click_login(driver, "登录")
        sleep(10)