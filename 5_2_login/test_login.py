from selenium import webdriver
from time import sleep
from config.driver_config import DriverConfig

driver = DriverConfig().driver_config()
driver.get('http://192.168.0.112')
driver.find_element_by_xpath("//input[@placeholder='用户名']").send_keys("周杰伦")
sleep(1)
driver.find_element_by_xpath("//input[@placeholder='密码']").send_keys("123456")
sleep(1)
driver.find_element_by_xpath("//span[text()='登录']/parent::button").click()
sleep(2)
driver.quit()
