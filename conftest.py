from time import sleep

import pytest
from selenium import webdriver


def check_lang(lang):
    languages = ['ar', 'ca', 'cs', 'da', 'de', 'el', 'es', 'fi',
                 'fr', 'it', 'ko', 'nl', 'pl', 'pt', 'ro', 'ru', 'sk', 'uk']
    if lang not in languages:
        raise ValueError(f'There is no such language "{lang}"')


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help='Set language: ru, es, en-gb')


@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption('language')
    check_lang(lang)
    link = f'http://selenium1py.pythonanywhere.com/{lang}/catalogue/coders-at-work_207/'
    browser = webdriver.Chrome()
    browser.get(link)
    sleep(30)
    yield browser
    browser.quit()
