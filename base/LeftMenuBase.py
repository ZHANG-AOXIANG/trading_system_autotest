# @PURPOSE: location on left menu
# @AUTHOR: Aoxiang Zhang
# @TIME: 15:31 2024/5/2 UTC+8

class LeftMenuBase:
    def level_one_menu(self, menu_name: str):
        """
        :param menu_name: level one menu name
        :return: xpath of level one menu
        """

        return "//aside[@class='el-aside']//span[text()='" + menu_name + "']/ancestor::li"

    def level_two_menu(self, menu_name: str):
        """
        :param menu_name: level two menu name
        :return: xpath of level two menu
        """

        return "//aside[@class='el-aside']//span[text()='" + menu_name + "']/ancestor::li[1]"
