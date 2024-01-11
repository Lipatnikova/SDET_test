from pages.base_page import BasePage
from locators.form_page_locators import PracticeFormLocators as Locator
from generator.generator import get_person


class FormsPage(BasePage):
    def fill_first_name(self):
        info = next(get_person())
        first_name = info.first_name
        self.send_keys_in_field(Locator.FIRST_NAME, first_name)
        return first_name

    def fill_last_name(self):
        info = next(get_person())
        last_name = info.last_name
        self.send_keys_in_field(Locator.LAST_NAME, last_name)
        return last_name

    def fill_email(self):
        info = next(get_person())
        email = info.email
        self.send_keys_in_field(Locator.EMAIL, email)
        return email

    def choose_gender(self):
        locator = Locator.GENDER
        gender_click = self.click_button(locator)
        gender_text = self.get_text(locator)
        return gender_text

    def fill_mobile_number(self):
        info = next(get_person())
        mobile = info.mobile
        self.send_keys_in_field(Locator.PHONE_NUMBER, mobile)
        return mobile[:10]



