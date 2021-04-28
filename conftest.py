import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser_name",
                     action="store",
                     default="chrome",
                     help="Choose browser: Chrome or Firefox")
    parser.addoption("--language",
                     action="store",
                     default="eu",
                     help="Choose language: ru, en, ....")


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == 'chrome':
        options = Options()
        options.add_experimental_option('prefs',
                                        {'intl.accept_languages': user_language})
        print("\n\nStart chrome browser for test...")
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', user_language)
        print('\n\nStart firefox browser for test...')
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        print(f'Browser "{browser_name}" is not supported by this test! Chrome of Firefox only!')
    yield browser
    print('\nQuit browser...')
    browser.quit()
