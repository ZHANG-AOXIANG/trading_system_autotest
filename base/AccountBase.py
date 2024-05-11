# @PURPOSE:
# @AUTHOR: Aoxiang Zhang
# @TIME: 23:31 2024/5/11 UTC+8

class AccountBase:
    def basic_info_profile_input(self):
        """
        get the xpath of profile image input box
        """
        return "//input[@type='file']"

    def basic_info_save_button(self):
        """
        get the xpath of save button in user basic infor page
        """
        return "//span[text()='保存']/parent::button"
