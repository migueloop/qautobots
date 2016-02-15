from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select as WebElementSelect

from qautobots.framework.helpers import take_screenshot


class Base(object):
    """Base element object.

    An Element object is the representation of a single element on a page. This
    could be a text input field, button, or any other user interface element
    that lives on a web page.

    """
    method = 'find_element_by_css_selector'

    def __get__(self, obj, cls=None):
        """Finds an element on the DOM and returns a Selenium.WebElement.

        Getting an element's value will use Selenium to find the object on the
        DOM and return the Selenium.WebElement found with its locator.

        """
        try:
            element = self.get_element(obj)
            return element

        except NoSuchElementException as error:
            screenshot = take_screenshot(obj.browser)
            error.msg = '{0} {1}:{2} not found on {3}. Screenshot: {4}'\
                .format(
                    error.msg,
                    self.__class__.__name__,
                    self.locator,
                    cls.__name__,
                    screenshot)
            raise error

    def __set__(self, obj, value):
        """Finds an element on the DOM and set is value.

        Setting an element's value will use Selenium to find the object on the
        DOM based on its locator. It will then set its value using send_keys.

        """
        element = self.get_element(obj)
        element.clear()
        element.send_keys(value)

    @classmethod
    def get_element(cls, obj):
        return getattr(obj.browser, cls.method)(cls.locator)


class ReadOnly(Base):
    """An element that can only be read otherwise a AttributeError is thrown"""

    def __set__(self, obj, value):
        raise AttributeError


class List(Base):
    """List of elements object

    A list object is a collection of Selenium.WebElement objects on a page.
    These elements have a common CSS selector.

    """
    method = 'find_elements_by_css_selector'


class Select(Base):
    """Select element which contains elements or options to select"""

    def __get__(self, obj, cls=None):
        """Finds an element on the DOM and return as Select"""
        element = super(Select, self).__get__(obj, cls)
        return WebElementSelect(element)

    def __set__(self, obj, value):
        """Finds an element in the DOM and set the value

        The value of the select element is selected by visible text
        of the options

        """
        element = self.get_element(obj)
        select = WebElementSelect(element)
        select.select_by_visible_text(value)


class Radio(List):
    """Radio element which inherit from List"""

    def __set__(self, obj, value):
        """Find radio element in the DOM and set by value of the element"""
        for element in self.get_element(obj):
            if element.get_attribute('value') == value:
                element.click()
