# Тестовое задание на практикум 
 _по автоматизации тестирования (SDET) от SimbirSoft_

![Python Version](https://img.shields.io/badge/python-3.10-blue)
[![dependency - selenium](https://img.shields.io/badge/dependency-selenium-blue?logo=selenium&logoColor=white)](https://pypi.org/project/selenium)
[![dependency - pytest](https://img.shields.io/badge/dependency-pytest-blue?logo=pytest&logoColor=white)](https://pypi.org/project/pytest)
[![dependency - Faker](https://img.shields.io/badge/dependency-Faker-blue)](https://pypi.org/project/Faker)
[![dependency - allure-pytest](https://img.shields.io/badge/dependency-allure--pytest-blue?logo=qameta&logoColor=white)](https://pypi.org/project/allure-pytest)

Status of Last Deployment: [![DEMOQA](https://github.com/Lipatnikova/SDET_test/actions/workflows/demoqa_push.yml/badge.svg?branch=)](https://github.com/Lipatnikova/SDET_test/actions/workflows/demoqa_push.yml)

## How to work with this repository:

- Clone repository to your machine.
- Navigate to the root folder of the project.
- Create a virtual environment.
- Run command **pip install -r requirements.txt**
- After, execute **pytest -s -v** to run tests.
- After, execute **pytest --alluredir=allure_result .\tests** to run tests.
- To view the allure report, type the command: **allure serve .\allure_result**


## Task description:


1. На Python (рекомендуется использовать версию 3.10) создать проект UI-автотестов по тест-кейсам описанным ниже.
2. В проекте использовать:
- Selenium Webdriver (желательно использовать браузер Chrome).
- При поиске элементов на странице использовать как минимум по одному селектору из перечисленных: css, xpath, id.
- Тестовый фреймворк Python – pytest.
3. Результаты оформить в виде проекта на GitHub.
4. В проекте желательно использовать паттерн проектирования Page Object Model.
5. Приветствуется, но не обязательно, реализация формирования отчетов о пройденных тестах через Allure.


### Кейс. Заполнение формы регистрации

**Предусловие:**
1. Открыть браузер
2. Перейти на страницу входа: https://demoqa.com/automation-practice-form

**Шаги:**
1. Заполнить поле First Name произвольной строкой
2. Заполнить поле Last Name произвольной строкой
3. Заполнить поле Email строкой формата name@example.com
4. Выбрать любое значение в Gender с помощью переключателя
5. Заполнить поле Mobile произвольными 10 цифрами
6. Заполнить поле Date of birth произвольной датой с помощью всплывающего календаря 
7. Заполнить поле Subjects произвольной строкой
8. Загрузить любое изображение в поле Picture
9. Заполнить поле Current Address произвольной строкой
10.Выбрать любое значение в Select State с помощью выпадающего списка
11.Выбрать любое значение в Select City с помощью выпадающего списка
12.Нажать кнопку Submit

**Ожидаемый результат:**
1. Появилось всплывающее окно с заголовком Thanks for submitting the form
2. В таблице на окне отображаются введенные ранее значения


