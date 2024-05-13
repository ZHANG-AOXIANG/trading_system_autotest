# @PURPOSE:
# @AUTHOR: Aoxiang Zhang
# @TIME: 22:18 2024/5/13 UTC+8

import pytest

from config.WebdriverConfig import WebdriverConfig

@pytest.fixture()
def driver(self):
    get_driver = WebdriverConfig().webdirver_config()
    yield get_driver
    get_driver.quit()