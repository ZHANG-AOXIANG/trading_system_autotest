# @PURPOSE: functions from repackaging selenium. recommend to visit https://github.com/seleniumbase/SeleniumBase
# @AUTHOR: Aoxiang Zhang
# @TIME: 00:46 2024/5/5 UTC+8

import time
from selenium.common.exceptions import ElementNotVisibleException, WebDriverException, NoSuchElementException, \
    StaleElementReferenceException
from selenium.webdriver.common.keys import Keys

import logs
from common.yaml_config import GetConf


class ObjectMap:
    base_url = GetConf().get_url()

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

    def go_to_url(self,
                  driver,
                  url,
                  locate_type_disappear=None,
                  locate_expression_disappear=None,
                  locate_type_appear=None,
                  locate_expression_appear=None):
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
            driver.get(self.base_url + url)
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

    def is_element_display(self, driver, locate_type, locate_expression):
        """
        check if the element is displayed
        :param driver: browser driver
        :param locate_type: id, name, class, xpath, css, ...
        :param locate_expression: the value of locate_type
        :return: True if the element is displayed, False if the element is not displayed
        """
        try:
            driver.find_element(by=locate_type, value=locate_expression)
            return True
        except NoSuchElementException:
            return False

    def fill_value(self, driver, locate_type, locate_expression, value, timeout=30):
        """
        fill value into the element
        :param driver: browser driver
        :param locate_type: id, name, class, xpath, css, ...
        :param locate_expression: the value of locate_type
        :param value: the value to fill
        :param timeout: the max time to wait
        :return: True
        """
        element = self.get_element(driver, locate_type=locate_type, locate_expression=locate_expression,
                                   timeout=timeout)
        try:
            element.clear()
        except StaleElementReferenceException:
            self.wait_for_completing_page_loading(driver=driver)
            time.sleep(0.06)
            element = self.wait_for_element_appear(driver, locate_type=locate_type, locate_expression=locate_expression,
                                                   timeout=timeout)
            try:
                element.clear()
            except Exception:
                pass
        except Exception:
            pass

        if type(value) is int or type(value) is float:
            value = str(value)

        try:
            if not value.endswith("/n"):
                element.send_keys(value)
                self.wait_for_completing_page_loading(driver=driver)
            else:
                value = value[:-1]
                element.send_keys(value)
                element.send_keys(Keys.ENTER)
                self.wait_for_completing_page_loading(driver=driver)
        except StaleElementReferenceException:
            self.wait_for_completing_page_loading(driver=driver)
            time.sleep(0.06)
            element = self.wait_for_element_appear(driver=driver, locate_type=locate_type,
                                                   locate_expression=locate_expression)
            element.clear()
            if not value.endswith("/n"):
                element.send_keys(value)
                self.wait_for_completing_page_loading(driver=driver)
            else:
                value = value[:-1]
                element.send_keys(value)
                element.send_keys(Keys.ENTER)
                self.wait_for_completing_page_loading(driver=driver)
        except Exception:
            raise Exception("It is failed to fill value into the element, locate type: " + locate_type +
                            "\nlocate_expression: " + locate_expression + "\nvalue: " + value)
        return True

    def element_click(
            self,
            driver,
            locate_type,
            locate_expression,
            locate_type_disappear=None,
            locate_expression_disappear=None,
            locate_type_appear=None,
            locate_expression_appear=None,
            timeout=30
    ):
        """
        click the element
        :param driver: browser driver
        :param locate_type: id, name, class, xpath, css, ...
        :param locate_expression: the value of locate_type
        :param locate_type_disappear: locate type of element when waiting for the element disappear
        :param locate_expression_disappear: expression of element when waiting for the element disappear
        :param locate_type_appear: locate type of element when waiting for the element appear
        :param locate_expression_appear: expression of element when waiting for the element appear
        :param timeout: the max time to wait
        :return: True
        """

        # element must appear
        element = self.wait_for_element_appear(
            driver=driver,
            locate_type=locate_type,
            locate_expression=locate_expression,
            timeout=timeout,
        )
        try:
            element.click()
        except StaleElementReferenceException:
            self.wait_for_completing_page_loading(driver=driver)
            time.sleep(0.06)
            element = self.wait_for_element_appear(
                driver=driver,
                locate_type=locate_type,
                locate_expression=locate_expression,
                timeout=timeout
            )
            element.click()
        except Exception as e:
            print("Page exception, it can not to click element", e)
            return False
        try:
            # after clicking, one element on old page disappear, one element on new page appear
            self.wait_for_element_disappear(
                driver=driver,
                locate_type=locate_type_disappear,
                locate_expression=locate_expression_disappear,
            )
            self.wait_for_element_appear(
                driver=driver,
                locate_type=locate_type_appear,
                locate_expression=locate_expression_appear,
            )
        except Exception as e:
            print("It is failed to wait element disappear or appear", e)
            return False

        return True

    def upload_file(self, driver, locate_type, locate_expression, file_path):
        """
        upload file
        :param driver: browser's driver
        :param locate_type: locator's  type
        :param locate_expression: locator's expression
        :param file_path: file's path
        :return
        """
        upload_element = self.get_element(driver, locate_type, locate_expression)
        return upload_element.send_keys(file_path)

    def switch_window_to_latest(self, driver):
        """
        switch handle to the latest window
        :param driver: browser's driver
        return
        """
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[-1])

    def into_iframe(self,driver,locate_iframe_type,locate_iframe_expression):
        """
        switch to iframe
        :param driver: browser's driver
        :param locate_iframe_type: type of locating iframe
        :param locate_iframe_expression: expression of locating iframe
        """
        iframe=self.get_element(driver,locate_iframe_type,locate_iframe_expression)
        driver.switch_to.frame(iframe)

    def out_from_iframe(self,driver):
        """
        switch out from iframe
        :param driver: browser's driver
        """
        driver.switch_to.parent_frame()

