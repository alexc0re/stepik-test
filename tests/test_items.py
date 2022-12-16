from selenium.webdriver.common.by import By
import time

def test_button_visibility(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(10)
    assert browser.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket').is_displayed(), \
        'No buttonn found'


