# @PURPOSE:
# @AUTHOR: Aoxiang Zhang
# @TIME: 23:37 2024/5/11 UTC+8

from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.AccountBase import AccountBase
from common.tools import get_img_path


class AccountPage(ObjectMap, AccountBase):
    def upload_profile_img(self, driver, profile_img_name):
        """
        upload profile image
        :param driver: browser's driver
        :param profile_img_name: profile image's name
        """
        profile_img_name_path = get_img_path(profile_img_name)
        upload_button_xpath = self.basic_info_profile_input()
        return self.upload_file(driver, By.XPATH, upload_button_xpath, profile_img_name_path)

    def click_save(self, driver):
        """
        click save button in basic user infor page
        :param driver: browser's driver
        """
        save_button_xpath = self.basic_info_save_button()
        return self.element_click(driver, By.XPATH, save_button_xpath)
