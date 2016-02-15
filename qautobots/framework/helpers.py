from __future__ import unicode_literals

from uuid import uuid4
import os

from qautobots.framework.qanfig import _merge_dicts, get_config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def take_screenshot(browser, fname=None):
    """Take Screenshot"""
    screenshot_dir = 'reports/screenshots'
    if not fname:
        fname = uuid4()
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    browser.save_screenshot('{0}/{1}.png'.format(screenshot_dir, fname))
    return '{0}.png'.format(fname)


def wait_for_element(browser, locator, timeout=5):
    """Wait until element present

    Keyword Arguments:
    browser - browser object
    locator - css locator of the element
    timeout - time to wait (in second) (default: 5)

    Return WebElement
    """
    wait = WebDriverWait(browser, timeout)
    element = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, locator)))
    return element


def wait_for_visibility(browser, locator, timeout=10):
    wait = WebDriverWait(browser, timeout)
    element = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, locator)))
    return element


def scroll_element_into_view(browser, element):
    """Scroll element into view"""
    y = element.location['y']
    browser.execute_script('window.scrollTo(0, {0})'.format(y))


def get_dark_flag(flag):
    """Return Dark Flag for specified flag"""
    darkFlags = get_config()
    return darkFlags['darkflags'][flag]


def get_application_settings():
    """Reads environment variables to retrieve application settings.

    This method will return an object of application settings retrieved from
    environment variables. A default value will be used if one is not found.

    """
    config = get_config()
    protocol = config['application']['protocol']
    if 'port' in config['application']:
        host = '{url}:{port}'.format(**config['application'])
    else:
        host = config['application']['url']

    if 'env' in config['application']:
        # env = '?forceenv={env}'.format(**config['application'])
        env = ''
    else:
        env = ''

    return {'protocol': protocol, 'host': host, 'env': env}


def get_desired_capabilities():
    """Return an object that specifies the desired capabilities.

    Read environment variables that specify how the Selenium test
    should be run. Return a dictionary representation of those values.

    """
    config = get_config()
    browser = config['selenium']['browser']
    desired_capabilities = getattr(
        webdriver.DesiredCapabilities, browser)
    desired_capabilities = _merge_dicts(
        desired_capabilities, config['selenium'])
    return desired_capabilities


def get_selenium_url():
    """Return a URL where the selenium grid can be found."""
    config = get_config()['selenium']

    profile = ''
    if config['hub']['provider'] == 'sauce':
        profile = "{user}:{key}@".format(**config['sauce'])

    command_executor = "http://{0}{url}:{port}/wd/hub".format(
        profile, **config['hub'])
    return str(command_executor)
