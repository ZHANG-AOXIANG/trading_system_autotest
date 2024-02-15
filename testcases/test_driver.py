# @PURPOSE:
# @AUTHOR: Aoxiang Zhang
# @TIME: 23:42 2024/2/2 UTC+8

from time import sleep

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
# set the browser windows size
chrome_options.add_argument("windows-size=1920,1080")

'''
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


driver_chrome = webdriver.Chrome(
    executable_path="/Users/aoxiang/PycharmProjects/trading_system_autotest/driver_files/chromedriver",
    options=chrome_options)
print("1")
driver_chrome.get("http://192.168.0.119/")
sleep(30)
driver_chrome.quit()
