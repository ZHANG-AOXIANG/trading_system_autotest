# @PURPOSE: functions in Home->Sold Goods page
# @AUTHOR: Aoxiang Zhang
# @TIME: 15:55 2024/5/2 UTC+8

class SoldGoodsBase:

    def top_options_row(self, option_name: str):
        """
        :param option_name: option name on top row, such as "全部","待付款"...
        :return:
        """

        return "//div[@class='el-tabs__nav is-top']//div[text()='" + option_name + "']"
