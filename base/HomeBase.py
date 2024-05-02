# @PURPOSE: functions in home page
# @AUTHOR: Aoxiang Zhang
# @TIME: 13:06 2024/5/2 UTC+8

class HomeBase:

    def wallet_switch_button(self):
        """
        @PURPOSE: wallet switch button in home page
        @RETURN: Xpath for wallet switch button
        """

        # return "//span[contains(@class,"switch")]"
        return "//span[@class='el-switch__core']"

    def logo_icon(self):
        """
        @PURPOSE: logo icon in home page
        @RETURN: Xpath for logo icon
        """

        return "//div[contains(text(),'二手')]"

    def welcome_message(self):
        """
        @PURPOSE: welcome message in home page
        @RETURN: Xpath for welcome message
        """

        # return "//div[@class='card_div']/span"
        return "//span[starts-with(text(), '欢迎您回来')]"

    def date_display_area(self):
        """
        @PURPOSE: date display area in home page
        @RETURN: Xpath for data display area
        """

        # return "//div[@class='date_half']"
        return "//div[@class='calender']/following-sibling::div"
