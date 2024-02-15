from selenium import webdriver
from config.driver_config import DriverConfig

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")


