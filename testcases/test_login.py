# @PURPOSE:
# @AUTHOR: Aoxiang Zhang
# @TIME: 21:11 2024/2/4 UTC+8

from time import sleep

from page.LoginPage import LoginPage


class TestLogin:

    def test_login(self, driver):
        LoginPage().login(driver, "jay")
        sleep(3)
        driver.quit()
