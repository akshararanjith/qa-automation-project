# import pytest
# from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()


def test_valid_login(driver):

    driver.get("https://the-internet.herokuapp.com/login")

    login_page = LoginPage(driver)
    login_page.login("tomsmith", "SuperSecretPassword!")

    assert "You logged into a secure area!" in driver.page_source