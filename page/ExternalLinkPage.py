# @PURPOSE:
# @AUTHOR: Aoxiang Zhang
# @TIME: 22:29 2024/5/11 UTC+8

from base.ObjectMap import ObjectMap


class ExternalLinkPage(ObjectMap):

    def goto_imooc(self, driver):
        """
        switch the window to imooc
        :param driver: browser's driver
        return
        """
        self.switch_window_to_latest(driver)
        return driver.title
