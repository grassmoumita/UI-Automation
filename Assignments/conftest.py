import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service(
            "C:/Users/moumitajoardar/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)

    elif browser_name == "firefox":
        service_obj = Service(
            "C:/Users/moumitajoardar/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
        driver = webdriver.Firefox(service=service_obj)

    driver.implicitly_wait(5)
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()

    request.cls.driver = driver  # to use this driver variable in other testcases where this fixture will use
    # yield
    # driver.close()

