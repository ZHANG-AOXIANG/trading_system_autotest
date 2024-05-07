# @PURPOSE: functions from repackaging selenium. recommend to visit https://github.com/seleniumbase/SeleniumBase
# @AUTHOR: Aoxiang Zhang
# @TIME: 00:46 2024/5/5 UTC+8

import time
from selenium.common.exceptions import ElementNotVisibleException, WebDriverException
from common.yaml_config import GetConf


class ObjectMap:
    url = GetConf.get_url()

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

    def wait_for_completing_page_loading(self, driver, timeout=10):
        """
        Wait for the page loading to complete
        :param driver: browser driver
        :param timeout: the max time to wait
        :return:
        """
        start_ms = time.time() * 1000  # start time
        stop_ms = start_ms + (timeout * 1000)  # stop time
        for x in range(int(timeout * 10)):
            try:
                # get the state of web page
                state = driver.execute_script("return document.readyState;")
            except WebDriverException:
                # js command will be failed to execute if there is issue from Driver. just skip and return True
                time.sleep(0.1)
                return True
            if state == "complete":
                return True
            else:
                now_ms = time.time() * 1000
                if now_ms >= stop_ms:
                    break
                time.sleep(0.1)
                pass
            time.sleep(0.1)
        raise Exception("It is failed to wait for page loading to complete after " + str(timeout) + " s.")

    def wait_for_element_disappear(self, driver, locate_type, locate_expression, timeout=10):
        """
        wait for the element disappearing
        :param driver: browser driver
        :param locate_type: id, name, class, xpath, css, ...
        :param locate_expression: the value of locate_type
        :param timeout: the max time to wait
        :return: True if the element disappear, False if the element is still visible
        """
        if locate_type:
            start_ms = time.time() * 1000  # start time
            stop_ms = start_ms + (timeout * 1000)  # stop time
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type, value=locate_expression)
                    if element.is_displayed():
                        now_ms = time.time() * 1000
                        if now_ms >= stop_ms:
                            break
                        time.sleep(0.1)
                except Exception:
                    return True
            raise Exception(
                "Element is not disappear, locate type: " + locate_type + "\nlocate_expression: " + locate_expression)
        else:
            pass

    def wait_for_element_appear(self, driver, locate_type, locate_expression, timeout=30):
        """
        Wait for element appear
        :param driver: browser driver
        :param locate_type: id, name, class, xpath, css, ...
        :param locate_expression: the value of locate_type
        :param timeout: the max time to wait
        :return: element
        """
        if locate_type:
            start_ms = time.time() * 1000
            stop_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type, value=locate_expression)
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
                except Exception:
                    now_ms = time.time() * 1000
                    if now_ms >= stop_ms:
                        break
                    time.sleep(0.1)
                    pass
            raise ElementNotVisibleException(
                "Element does not appear, locate type: " + locate_type + " locate expression: " + locate_expression)
        else:
            pass

    def go_to_url(self, driver, url, locate_type_disappear=None, locate_expression_disappear=None,
                  locate_type_appear=None, locate_expression_appear=None):
        """
        go to url
        :param driver: driver of browser
        :param url: the goal address
        :param locate_type_disappear: locate type of element when waiting for the element disappear
        :param locate_expression_disappear: expression of element when waiting for the element disappear
        :param locate_type_appear: locate type of element when waiting for the element appear
        :param locate_expression_appear: expression of element when waiting for the element appear
        :return True

        """
        try:
            driver.get(self.url + url)
            # waiting  the new page complete loading
            self.wait_for_completing_page_loading(driver)
            # check the element in old page disappear
            self.wait_for_element_disappear(driver, locate_type_disappear, locate_expression_disappear)
            # check the element in new page appear
            self.wait_for_element_appear(driver, locate_type_appear, locate_expression_appear)
        except Exception as e:
            print("it is failed to go to url, reasons: " + str(e))
            return False
        return True
