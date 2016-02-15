from __future__ import unicode_literals

import time

from qautobots.pages.helloworld import HelloWorld
from qautobots.tests.base_test import BaseTest


class WhenGoingToHelloWorld(BaseTest):

	@classmethod
	def setUpTest(cls):
		# set up test here
		world = HelloWorld(cls.browser)
		time.sleep(2)
		world.side_menu[0].click()
		time.sleep(2)

	def should_do_something_hello_worldly(self):
		# add asserts here
		self.assertIn('/what-we-do/', self.browser.current_url)
