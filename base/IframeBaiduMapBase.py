# @PURPOSE:
# @AUTHOR: Aoxiang Zhang
# @TIME: 00:07 2024/5/12 UTC+8

class IframeBaiduMapBase:
    def search_button_xpath(self):
        """
        get xpath of search button in baidu map iframe
        """
        return "//button[@id='search-button']"

    def baidu_map_iframe_xpath(self):
        """
        get xpath of baidu map iframe
        """
        return "//iframe[@src='https://map.baidu.com/']"
