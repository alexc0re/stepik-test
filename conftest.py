import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en or es")


@pytest.fixture(scope="function")
def browser(request):
    browser_lang = request.config.getoption("language")
    browser = None
    if browser_lang:
        print("\nstart ES chrome browser for test..")
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_lang})
        browser = webdriver.Chrome(options=options)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
