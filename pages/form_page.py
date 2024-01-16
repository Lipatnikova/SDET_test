import allure
import random
import pathlib

from pathlib import Path
from pages.base_page import BasePage
from locators.form_page_locators import PracticeFormLocators as Locator
from generator.generator import get_person, generated_subject, generated_city
from selenium.webdriver import Keys


class FormPage(BasePage):
    def fill_first_name(self):
        info = next(get_person())
        first_name = info.first_name
        with allure.step("Заполнить поле First Name произвольной строкой"):
            self.send_keys_in_field(Locator.FIRST_NAME, first_name)
        return first_name

    def fill_last_name(self):
        info = next(get_person())
        last_name = info.last_name
        with allure.step("Заполнить поле Last Name произвольной строкой"):
            self.send_keys_in_field(Locator.LAST_NAME, last_name)
        return last_name

    def fill_email(self):
        info = next(get_person())
        email = info.email
        with allure.step("Заполнить поле Email строкой формата name@example.com"):
            self.send_keys_in_field(Locator.EMAIL, email)
        return email

    def choose_gender(self):
        locator = Locator.GENDER
        with allure.step("Выбрать любое значение в Gender"):
            self.click_button(locator)               # gender click
        gender_text = self.get_text(locator)
        return gender_text

    def fill_mobile_number(self):
        info = next(get_person())
        mobile = info.mobile
        with allure.step("Заполнить поле Mobile произвольными 10 цифрами"):
            self.send_keys_in_field(Locator.PHONE_NUMBER, mobile)
        return mobile[:10]

    def choose_date_of_birth(self):
        with allure.step("Заполнить поле Date of birth произвольной датой"):
            self.click_element(Locator.BIRTH_DAY)    # choose calender
            # Select year:
            self.click_button(Locator.YEARS_CHANGE)
            year = self.get_text(Locator.YEARS)
            self.click_element(Locator.YEARS)        # choose years
            # Select month:
            self.click_element(Locator.MONTHS_CHANGE)
            month = self.get_text(Locator.MONTHS)
            self.click_element(Locator.MONTHS)        # choose month
            # Select day:
            day = self.click_random_element_day(Locator.DAY_DATE_PICKER)
        return day, f'{month},{year}'

    def fill_subjects(self):
        with allure.step("Заполнить поле Subjects произвольной строкой"):
            subject_list = generated_subject()
            for item in subject_list:
                self.send_keys_in_field(Locator.SUBJECT, item)
                self.send_keys_in_field(Locator.SUBJECT, Keys.RETURN)
        return subject_list

    def choose_hobby(self):
        with allure.step("Выбрать любое значение Hobbies"):
            locator = Locator.HOBBIES
            self.click_button(locator)                # choose hobby
        return self.get_text(locator)

    def select_picture(self):
        with allure.step("Загрузить любое изображение в поле Picture"):
            file_name = "img_for_test.jpg"
            # Получаем строку, содержащую путь к рабочей директории:
            dir_path = pathlib.Path.home()
            # Объединяем полученную строку с недостающими частями пути
            path = Path(dir_path, 'work', 'SDET_test', 'SDET_test', 'tests', 'resource', file_name)
            self.send_keys_in_field(Locator.FILE_INPUT, rf'{str(path)}')
        return file_name

    def fill_current_address(self):
        info = next(get_person())
        current_address = info.current_address
        with allure.step("Заполнить поле Current Address произвольной строкой"):
            self.send_keys_in_field(Locator.CURRENT_ADDRESS, current_address)
        return current_address

    def select_state_and_city(self):
        with allure.step("Выбрать любое значение в Select State и Select City"):
            state, city = generated_city()
            new_city = city[random.randint(0, len(city) - 1)]
            self.click_element(Locator.SELECT_STATE)
            self.send_keys_in_field(Locator.STATE_INPUT, state)
            self.send_keys_in_field(Locator.STATE_INPUT, Keys.RETURN)
            self.click_element(Locator.SELECT_CITY)
            self.send_keys_in_field(Locator.CITY_INPUT, new_city)
            self.send_keys_in_field(Locator.CITY_INPUT, Keys.RETURN)
        return state, new_city

    def click_submit(self):
        with allure.step("Нажать кнопку Submit"):
            self.element_is_visible(Locator.SUBMIT).send_keys(Keys.RETURN)

    @property
    def get_modal_title(self):
        return self.get_text(Locator.TITLE_MODAL)
