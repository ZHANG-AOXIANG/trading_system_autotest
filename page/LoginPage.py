# @PURPOSE: process steps about login in page
# @AUTHOR: Aoxiang Zhang
# @TIME: 21:05 2024/2/4 UTC+8

from base.LoginBase import LoginBase


class LoginPage(LoginBase):
    def login_input_value(self, driver, input_placeholder, input_value):
        '''
        input value in login page
        :param driver:
        :param input_placeholder:
        :param input_value:
        :return:
        '''
        input_xpath = self.login_input(input_placeholder)
        return driver.find_element_by_xpath(input_xpath).send_keys(input_value)

    def click_login(self, driver, button_name):
        '''
        click login in button
        :param driver:
        :param button_name:
        :return:
        '''
        button_xpath = self.login_button(button_name)
        return driver.find_element_by_xpath(button_xpath).click()
