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
        #driver.get("http://192.168.0.121/login")
        LoginPage().login(driver,"jay")
        sleep(3)
        driver.quit()

