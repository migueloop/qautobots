from __future__ import unicode_literals

import json
import requests
import socket

from qautobots import unittest
from qautobots.framework.connection import Browser
from qautobots.framework.driver import get_desired_capabilities
from qautobots.framework.helpers import take_screenshot


class BaseTest(unittest.TestCase):
    """Extending unittest in order to have more functionality"""

    @classmethod
    def setUpClass(cls):
        cls.browser = Browser()
        cls.setUpTest()

    @classmethod
    def setUpTest(cls):
        """Setup and initializing test"""
        pass

    @classmethod
    def tearDownClass(cls):
        cls.tearDownTest()
        cls.report_name()
        cls.browser.quit()

    @classmethod
    def tearDownTest(cls):
        """Tear down and clean up test"""
        pass

    @classmethod
    def report_name(cls):
        """Report test name to saucelabs"""
        modules = cls.__module__.split('.')
        fname = modules[-1]
        module = modules[-2]
        test_name = '{0}:{1}'.format(fname, cls.__name__)
        hostname = socket.gethostname()
        tags = [module, hostname]
        cls.post_sauce({'name': test_name, 'tags': tags})

    @classmethod
    def post_sauce(cls, data={}):
        pass
        capabilities = get_desired_capabilities()
        if capabilities['hub']['provider'] == 'sauce':
            user = capabilities['sauce']['user']
            key = capabilities['sauce']['key']
            headers = {'content-type': 'Content-Type:text/json'}
            uri = 'http://{0}:{1}@saucelabs.com/rest/v1/{0}/jobs/{2}'\
                .format(user, key, cls.browser.session_id)
            requests.put(uri, data=json.dumps(data), headers=headers)

    @property
    def failureException(self):
        class MyFailureException(AssertionError):
            def __init__(self_, *args, **kwargs):
                take_screenshot(browser=self.browser, fname=self.id())
                return super(MyFailureException, self_).\
                    __init__(*args, **kwargs)
        MyFailureException.__name__ = AssertionError.__name__
        self.post_sauce({'passed': False})
        return MyFailureException

    def assertIsDisplayed(self, element):
        """Custom assertion to check if the element is displayed"""
        self.assertTrue(element.is_displayed())
