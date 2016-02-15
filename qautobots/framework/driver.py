from __future__ import unicode_literals

from qautobots.framework.qanfig import _merge_dicts
from selenium.webdriver.remote.webdriver import WebDriver

from qautobots.framework.helpers import (
    get_desired_capabilities,
    get_selenium_url
)


class CustomDriver(WebDriver):
    def __init__(self, capabilities=None):
        capabilities = capabilities or {}
        caps = _merge_dicts(
            get_desired_capabilities(), capabilities)
        super(CustomDriver, self).__init__(
            desired_capabilities=caps,
            command_executor=get_selenium_url(),
        )
