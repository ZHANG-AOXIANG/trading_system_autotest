# @PURPOSE:
# @AUTHOR: Aoxiang Zhang
# @TIME: 22:43 2024/5/11 UTC+8

class OrderBase:
    def order_tab_button_xpath(self, button_name):
        """
        get the button's xpath in order page
        :param button_name: "全部", "待付款", "待发货", "运输中", "待确认", "待评价"
        :return :button's xpath
        """
        return "//div[@role='tab' and text()='" + button_name + "']"
