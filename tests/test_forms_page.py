import allure
from pages.form_page import FormPage
from data.data_urls import DataUrls
from data.data import ModalData


class TestFormPage:
    @allure.title("Проверка заголовка всплывающего окна")
    @allure.description("Проверка заголовка 'Thanks for submitting the form' после "
                        "заполнения Формы регистрации корректными данными")
    @allure.severity(allure.severity_level.MINOR)
    @allure.label("owner", "Липатникова А.В.")
    def test_verify_modal_title(self, driver):
        form_page = FormPage(driver, DataUrls.FORM_URL)
        form_page.open()
        first_name = form_page.fill_first_name()
        last_name = form_page.fill_last_name()
        email = form_page.fill_email()
        gender = form_page.choose_gender()
        mobile = form_page.fill_mobile_number()
        day, month, year = form_page.choose_date_of_birth()
        subject_list = form_page.fill_subjects()
        hobby = form_page.choose_hobby()
        # file_name = form_page.select_picture()
        address = form_page.fill_current_address()
        state, city = form_page.select_state_and_city()
        form_page.click_submit()
        with allure.step("Проверить всплывающее окно с заголовком Thanks for submitting the form"):
            assert form_page.get_modal_title == ModalData.EXPECTED_TITLE, \
                "Modal title is not displayed correctly or contains unexpected text"
