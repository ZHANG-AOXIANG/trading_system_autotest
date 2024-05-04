# @PURPOSE: functions from repackaging selenium. recommend to visit https://github.com/seleniumbase/SeleniumBase
# @AUTHOR: Aoxiang Zhang
# @TIME: 00:46 2024/5/5 UTC+8

import time
from selenium.common.exceptions import ElementNotVisibleException


class ObjectMap:

    def get_element(self, driver, locate_type, locate_expression, is_visible=False, timeout=10):
        """
        Get element from the page
        :param driver: browser driver
        :param locate_type: id, name, class, xpath, css, ...
        :param locate_expression: the value of locate_type
        :param is_visible: if the element is visible. False means that element is not visible
        :param timeout: the max time to wait
        :return: element
        """
        start_ms = time.time() * 1000  # start time
        stop_ms = start_ms + (timeout * 1000)  # stop time
        for x in range(int(timeout * 10)):
            try:
                element = driver.find_element(by=locate_type, value=locate_expression)
                time.sleep(0.1)
                # if the element is not visible, just return it
                if not is_visible:
                    return element
                # if the element is visible, it needs to check if it is displayed.
                else:
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
            except Exception:
                now_ms = time.time() * 1000
                if now_ms >= stop_ms:
                    break
                pass
            time.sleep(0.1)
        raise ElementNotVisibleException(
            "It is failed to locate element. Locate type: " + locate_type + ". Locate_expression: " + locate_expression)
