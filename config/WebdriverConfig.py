# @PURPOSE: web driver config
# @AUTHOR: Aoxiang Zhang
# @TIME: 16:28 2024/2/3 UTC+8


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class WebdriverConfig:
    """
    Browser driver config
    """

    def webdirver_config(self):
        url = "https://registry.npmmirror.com/-/binary/chromedriver"
        latest_release_url = "https://registry.npmmirror.com/-/binary/chromedriver/LATEST_RELEASE"
        driver = webdriver.Chrome(ChromeDriverManager(url=url, latest_release_url=latest_release_url).install())
        # delete all browser cookies
        driver.delete_all_cookies()
        return driver
