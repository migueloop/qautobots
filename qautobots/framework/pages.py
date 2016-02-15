from __future__ import unicode_literals

from datetime import timedelta
from time import sleep

from qautobots.framework.connection import CONFIG


class BasePage(object):
    """A base page object.

    A Page is a representation of a browser controlled web page. A page is
    typically comprised of Elements and functions that operate on that page.

    """
    def __init__(self, browser):
        self.browser = browser
        self.browser.navigate(self.url)

    def wait_for(self, func, *args, **kwargs):
        """Wait until a `func` returns without raising an AssertionError."""
        MAX_WAIT = CONFIG['page_load_time']
        SLEEP_INTERVAL = CONFIG['sleep_interval']

        max_wait = timedelta(0, MAX_WAIT, 0)
        elapsed_time = max_wait
        interval = timedelta(0, SLEEP_INTERVAL, 0)
        while elapsed_time:
            try:
                func(*args, **kwargs)
                return
            except AssertionError:
                sleep(SLEEP_INTERVAL)
                elapsed_time = elapsed_time - interval
        raise AssertionError


class BaseAuthPage(BasePage):
    """A base page object that has an authentication

    This page need a login name and password to acces it.
    When this page is accessed it will return a popup in the browser
    for authentication.

    """
    def __init__(self, browser, login='testing', password='testing'):
        self.browser = browser
        self.browser.navigate_with_auth(self.url, login, password)


class BaseWithHash(BasePage):
    """A base page object that requires a hash in the url"""
    def __init__(self, browser, url_hash=''):
        self.browser = browser
        self.url = '{0}?{1}'.format(self.url, url_hash)
        self.browser.go_to_url(self.url)
