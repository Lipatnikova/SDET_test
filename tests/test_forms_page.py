from pages.form_page import FormsPage
from data.data_urls import DataUrls


class TestFormsPage:
    def test_verify_fill_form_fields(self, driver):
        form_page = FormsPage(driver, DataUrls.FORM_URL)
        form_page.open()
        first_name = form_page.fill_first_name()
        last_name = form_page.fill_last_name()
        email = form_page.fill_email()
        gender = form_page.choose_gender()
        mobile = form_page.fill_mobile_number()
        day, month, year = form_page.choose_date_of_birth()
        subject_list = form_page.fill_subjects()
        hobby = form_page.choose_hobby()

