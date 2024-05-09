# @PURPOSE: web driver config
# @AUTHOR: Aoxiang Zhang
# @TIME: 16:28 2024/2/3 UTC+8


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class WebdriverConfig:
    """
    Browser driver config
    """

    '''
    chrome_options = webdriver.ChromeOptions()
    # set the browser windows size
    chrome_options.add_argument("windows-size=1920,1080")

    add_argument KEY 
    "excludeSwitches", ["enable-automation"] : remove notice about browser is controlled by automation
    "--ignore-certificate-errors" : solver the problem that Chrome can not access HTTPS
    "--allow-insecure-localhost" : allow to ignore the TLS/SSL errors in localhost
    "--incognito" : set Chrome browser to private mode
    "--headless" : set to headless mode
    "--disable-gpu" : improve process speed
    "--no-sandbox" : 
    "--disable-dev-shm-usage" : 
    '''

    def webdirver_config(self):

        url = "https://registry.npmmirror.com/-/binary/chromedriver"
        latest_release_url = "https://registry.npmmirror.com/-/binary/chromedriver/LATEST_RELEASE"
        driver = webdriver.Chrome(ChromeDriverManager(url=url, latest_release_url=latest_release_url).install())
        # delete all browser cookies
        #driver=(webdriver.Edge(executable_path=ChromeDriverManager().install()))
        driver.delete_all_cookies()
        return driver