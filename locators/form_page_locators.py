import random
from selenium.webdriver.common.by import By


class PracticeFormLocators:
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.XPATH, "//*[@id='userEmail']")
    GENDER = (By.CSS_SELECTOR, f"label[for='gender-radio-{random.randint(1, 3)}']")
    PHONE_NUMBER = (By.CSS_SELECTOR, "input[id='userNumber']")
    BIRTH_DAY = (By.CSS_SELECTOR, "input[id='dateOfBirthInput']")
    DAY_DATE_PICKER = (By.CSS_SELECTOR, ".react-datepicker__day")
    MONTHS_CHANGE = (By.CSS_SELECTOR, f"select[class='react-datepicker__month-select']")
    MONTHS = (By.CSS_SELECTOR,
              f"select[class='react-datepicker__month-select'] option[value='{random.randint(1, 12)}']")
    YEARS_CHANGE = (By.CSS_SELECTOR, f"select[class='react-datepicker__year-select']")
    YEARS = (By.CSS_SELECTOR,
             f"select[class='react-datepicker__year-select'] option[value='{random.randint(1940, 2023)}']")
    SUBJECT = (By.CSS_SELECTOR, "input[id='subjectsInput']")
    HOBBIES = (By.CSS_SELECTOR, f"label[for='hobbies-checkbox-{random.randint(1, 3)}']")
    FILE_INPUT = (By.CSS_SELECTOR, "input[id='uploadPicture']")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    SELECT_STATE = (By.CSS_SELECTOR, "div[id ='state']")
    STATE_INPUT = (By.CSS_SELECTOR, "input[id='react-select-3-input']")
    SELECT_CITY = (By.CSS_SELECTOR, "div[id ='city']")
    CITY_INPUT = (By.CSS_SELECTOR, "input[id='react-select-4-input']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    #modal
    TITLE_MODAL = (By.CSS_SELECTOR, "#example-modal-sizes-title-lg")
    VALUES_TABLE = (By.CSS_SELECTOR, "div.modal-body > div > table > tbody > tr > td:nth-child(2)")
