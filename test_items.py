from selenium.webdriver.common.by import By


def test_is_there_add_to_basket_btn(browser):
    button = browser.find_element(
        By.CSS_SELECTOR, '#add_to_basket_form button.btn')
    assert button.is_enabled(), "Button is disabled"
