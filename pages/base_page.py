import random

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        """
        This method opens a browser by the provided link
        """
        self.driver.get(self.url)

    def element_is_clickable(self, locator, timeout=10):
        """
        This method expects to verify that the element is visible, displayed on the page, and enabled.
        The element is present in the DOM tree.
        Locator - is used to find the element.
        Timeout - the duration it will wait for. The default is set to 10 seconds, but it can be modified if needed.
        """
        return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def element_is_present(self, locator, timeout=10):
        """
        This method expects to verify that the element is present in the DOM tree,
        but not necessarily visible and displayed on the page.
        Locator - is used to find the element.
        Timeout - the duration it will wait for. The default is set to 10 seconds, but it can be modified if needed.
        """
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_is_visible(self, locator, timeout=10):
        """
        This method expects to verify that the element is present in the DOM tree, visible, and displayed on the page.
        Visibility means that the element is not only displayed but also has a height and width greater than 0.
        Locator - is used to find the element.
        Timeout - the duration it will wait for. The default is set to 10 seconds, but it can be modified if needed.
        """
        self.go_to_element(self.element_is_present(locator))
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_present(self, locator, timeout=10):
        """
           This method expects to verify that the elements are present in the DOM tree,
           but not necessarily visible and displayed on the page.
           Locator - is used to find the elements.
           Timeout - the duration it will wait for. The default is set to 10 seconds, but it can be modified if needed.
           """
        return Wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def elements_are_visible(self, locator, timeout=10):
        """
        This method expects to verify that the elements are present in the DOM tree, visible and displayed on the page.
        Visibility means that the elements are not only displayed but also have a height and width greater than 0.
        Locator - is used to find the elements.
        Timeout - the duration it will wait for. The default is set to 10 seconds, but it can be modified if needed.
        """
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def go_to_element(self, element):
        """
        This method scrolls the page to the selected element, making it visible to the user.
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_text(self, locator):
        """
        This method gets the text from the element.
        """
        return self.element_is_visible(locator, 20).text

    def send_keys_in_field(self, locator, key):
        """
        This method sends the key in the field.
        """
        self.element_is_visible(locator, 20).send_keys(key)

    def click_button(self, locator):
        self.element_is_clickable(locator).click()

    def click_element(self, locator):
        self.element_is_visible(locator, 20).click()

    def click_random_element_day(self, locator):
        elements = self.elements_are_present(locator)
        random_element = random.choice(elements)
        text = random_element.text
        random_element.click()
        if len(text) == 1:
            text = f'0{text}'
        return text

