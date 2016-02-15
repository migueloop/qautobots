from __future__ import unicode_literals

from qautobots.framework import elements
from qautobots.framework.pages import BasePage
from qautobots.pages.locators import hello_world as locators


class SideMenu(elements.List):
	locator = locators['side_menu']
	

class HelloWorld(BasePage):

	url = 'http://www.helloworld.com/'

	# add page objects here
	side_menu = SideMenu()
	