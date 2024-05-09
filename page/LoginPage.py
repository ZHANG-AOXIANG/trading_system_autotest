# @PURPOSE: process steps about login in page
# @AUTHOR: Aoxiang Zhang
# @TIME: 21:05 2024/2/4 UTC+8

from selenium.webdriver.common.by import By
from base.LoginBase import LoginBase
from base.ObjectMap import ObjectMap
from common.yaml_config import GetConf
from config.WebdriverConfig import WebdriverConfig


class LoginPage(LoginBase, ObjectMap):
    def login_input_value(self, driver, input_placeholder, input_value):
        '''
        input value in login page
        :param driver:
        :param input_placeholder:
        :param input_value:
        :return:
        '''
        input_xpath = self.login_input(input_placeholder)
        # return driver.find_element_by_xpath(input_xpath).send_keys(input_value)
        return self.fill_value(driver=driver,
                               locate_type=By.XPATH,
                               locate_expression=input_xpath,
                               value=input_value)

    def click_login(self, driver, button_name):
        '''
        click login in button
        :param driver:
        :param button_name:
        :return:
        '''
        button_xpath = self.login_button(button_name)
        # return driver.find_element_by_xpath(button_xpath).click()
        return self.element_click(driver, By.XPATH, button_xpath)

    def login(self, driver, user):
        '''
        login in
        :param driver:
        :param user:
        :return:
        '''

        self.go_to_url(driver, '/login')
        username = GetConf().get_username(user)
        password = GetConf().get_password(user)
        self.login_input_value(driver, '用户名', username)
        self.login_input_value(driver, '密码', password)
        self.click_login(driver, '登录')
