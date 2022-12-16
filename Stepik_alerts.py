from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select



link = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))




try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    int(x)
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(x))
    browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()




finally:
    time.sleep(15)
    browser.quit()